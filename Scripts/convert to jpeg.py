"""
Usage:
    1. Set source_folder and destination_folder below.
    2. From the repository root, run:
           python "Scripts/convert to jpeg.py"

This script recursively copies existing JPEG files and converts PNG files to
JPEG files in a separate destination tree that mirrors the source folders.
PNG transparency is composited onto a white background before conversion, so
the resulting JPEGs have a valid opaque RGB format. It keeps a count of
converted files, copied files, and conversion errors, and reports progress
without modifying the source images.
"""

import os
import shutil
from PIL import Image

# This script recursively copies JPEG files and converts PNG files to JPEG,
# using a white background wherever transparency is present.
source_folder = r""
destination_folder = r""

# Create the destination folder if it does not exist.
if not os.path.exists(destination_folder):
    os.makedirs(destination_folder)
    print(f"Created destination folder: {destination_folder}")

# Counters used to report processing results.
converted_count = 0
copied_count = 0

# Recursively process PNG files, including all subdirectories.
for current_path, _, file_names in os.walk(source_folder):
    relative_path = os.path.relpath(current_path, source_folder)
    current_output_folder = (
        destination_folder
        if relative_path == os.curdir
        else os.path.join(destination_folder, relative_path)
    )
    os.makedirs(current_output_folder, exist_ok=True)

    for file_name in file_names:
        input_path = os.path.join(current_path, file_name)

        if file_name.lower().endswith((".jpg", ".jpeg")):
            output_path = os.path.join(current_output_folder, file_name)
            try:
                shutil.copy2(input_path, output_path)
                print(f"Copied unchanged: {input_path} -> {output_path}")
                copied_count += 1
            except Exception as error:
                print(f"Error copying {input_path}: {error}")

        elif file_name.lower().endswith(".png"):

            base_name = os.path.splitext(file_name)[0]
            output_path = os.path.join(
                current_output_folder, f"{base_name}.jpg"
            )

            try:
                with Image.open(input_path) as image:
                    # Convert transparent areas to a white background.
                    if image.mode in ("RGBA", "LA") or (
                        image.mode == "P" and "transparency" in image.info
                    ):
                        rgba_image = image.convert("RGBA")
                        background = Image.new(
                            "RGB", rgba_image.size, (255, 255, 255)
                        )
                        background.paste(rgba_image, mask=rgba_image.split()[3])
                        image = background
                    else:
                        image = image.convert("RGB")

                    image.save(output_path, "JPEG", quality=95)

                print(f"Converted: {input_path} -> {output_path}")
                converted_count += 1
            except Exception as error:
                print(f"Error converting {input_path}: {error}")

print(f"\nConversion completed! Converted {converted_count} images.")