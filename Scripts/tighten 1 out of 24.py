"""
Usage:
    1. Set SOURCE_FOLDER and DESTINATION_FOLDER below.
    2. From the repository root, run:
           python "Scripts/tighten 1 out of 24.py"

This script recursively finds supported image files in SOURCE_FOLDER and
recreates their folder structure under DESTINATION_FOLDER. Each image is
cropped by removing approximately 1/48 of its width from both the left and
right edges. The original files are not changed; processed images are written
to the destination, with JPEG transparency converted to a white-compatible
RGB image when necessary. A progress summary reports successful and failed
files.
"""

import os
from PIL import Image


# This script trims 1/48 of an image's width from both sides and saves the
# processed files in a separate directory while preserving the folder tree.
SOURCE_FOLDER = r"/SOURCE_FOLDER_PATH"
DESTINATION_FOLDER = r"/DESTINATION_FOLDER_PATH"

IMAGE_EXTENSIONS = (".jpg", ".jpeg", ".png", ".webp", ".bmp", ".tif", ".tiff")


def trim_image(input_path, output_path):
	"""Remove 1/48 of the image width from both the left and right edges."""
	with Image.open(input_path) as image:
		width, height = image.size
		trim_amount = max(1, round(width / 48))

		if width <= trim_amount * 2:
			raise ValueError("The image is not wide enough to remove both sections.")

		crop_area = (trim_amount, 0, width - trim_amount, height)
		cropped_image = image.crop(crop_area)

		# JPEG does not support transparency; other formats retain their mode.
		if output_path.lower().endswith((".jpg", ".jpeg")):
			if cropped_image.mode not in ("RGB", "L"):
				cropped_image = cropped_image.convert("RGB")
			cropped_image.save(output_path, quality=95)
		else:
			cropped_image.save(output_path)

		cropped_image.close()


def main():
	os.makedirs(DESTINATION_FOLDER, exist_ok=True)
	processed_count = 0
	error_count = 0

	for current_path, _, file_names in os.walk(SOURCE_FOLDER):
		relative_path = os.path.relpath(current_path, SOURCE_FOLDER)
		output_folder = (
			DESTINATION_FOLDER
			if relative_path == os.curdir
			else os.path.join(DESTINATION_FOLDER, relative_path)
		)
		os.makedirs(output_folder, exist_ok=True)

		for file_name in file_names:
			if not file_name.lower().endswith(IMAGE_EXTENSIONS):
				continue

			input_path = os.path.join(current_path, file_name)
			output_path = os.path.join(output_folder, file_name)

			try:
				trim_image(input_path, output_path)
				processed_count += 1
				print(f"Trimmed: {input_path} -> {output_path}")
			except Exception as error:
				error_count += 1
				print(f"Error processing {input_path}: {error}")

	print(f"\nCompleted: {processed_count} images processed, {error_count} errors.")


if __name__ == "__main__":
	main()
