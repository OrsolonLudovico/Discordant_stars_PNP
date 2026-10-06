from pathlib import Path
import msvcrt
import os
import tempfile

from PIL import Image


ESTENSIONI = {".jpg", ".jpeg", ".png", ".bmp", ".tif", ".tiff", ".webp"}


def scegli_rotazione() -> Image.Transpose:
	opzioni = [
		("90 gradi in senso orario", Image.Transpose.ROTATE_270),
		("90 gradi in senso antiorario", Image.Transpose.ROTATE_90),
	]
	selezionata = 0

	while True:
		print("\033[2J\033[H", end="")
		print("Scegli la rotazione e premi Invio:\n")
		for indice, (nome, _) in enumerate(opzioni):
			cursore = ">" if indice == selezionata else " "
			print(f"{cursore} {nome}")

		carattere = msvcrt.getwch()
		if carattere in ("\x00", "\xe0"):
			freccia = msvcrt.getwch()
			if freccia == "H":
				selezionata = (selezionata - 1) % len(opzioni)
			elif freccia == "P":
				selezionata = (selezionata + 1) % len(opzioni)
		elif carattere in ("\r", "\n"):
			return opzioni[selezionata][1]


def ruota_immagini(cartella: Path, rotazione: Image.Transpose) -> None:
	immagini = [
		file for file in cartella.rglob("*")
		if file.is_file() and file.suffix.lower() in ESTENSIONI
	]

	for file in immagini:
		try:
			with Image.open(file) as immagine:
				if immagine.width <= immagine.height:
					print(f"Lasciata invariata: {file}")
					continue

				metadati = immagine.info.copy()
				ruotata = immagine.transpose(rotazione)

				parametri = {}
				if file.suffix.lower() in {".jpg", ".jpeg"}:
					parametri["quality"] = 95
					parametri["optimize"] = True
				if "exif" in metadati:
					parametri["exif"] = metadati["exif"]

				with tempfile.NamedTemporaryFile(
					dir=file.parent,
					suffix=file.suffix,
					delete=False,
				) as temporaneo:
					percorso_temporaneo = Path(temporaneo.name)

				try:
					ruotata.save(percorso_temporaneo, **parametri)
					os.replace(percorso_temporaneo, file)
				except Exception:
					percorso_temporaneo.unlink(missing_ok=True)
					raise

			print(f"Ruotata: {file}")
		except Exception as errore:
			print(f"Saltata {file}: {errore}")


if __name__ == "__main__":
	percorso = Path(input("Percorso della cartella: ").strip().strip('"'))

	if not percorso.is_dir():
		print("La cartella indicata non esiste.")
	else:
		rotazione = scegli_rotazione()
		ruota_immagini(percorso, rotazione)
		print("Operazione completata.")
