# File Organiser

A simple Python script to organise files in a directory by their type (images, videos, documents, audio, etc.).

## Features
- Automatically sorts files into folders based on their extensions
- Customisable folder and extension mapping
- Simple command-line interface
- Tracks and displays the time taken to organise files

## Requirements
- Python 3.7+
- Standard library modules: `os`, `pathlib`, `shutil`, `typing`
- `timer.py` (included in this repo)

## Usage
1. **Clone or download this repository.**
2. **Ensure you have Python installed.**
3. **Run the script:**
   ```bash
   python main.py
   ```
4. **Follow the prompts:**
   - Press `Y` to use the current working directory, or enter a different path.
   - The script will create folders (if not present) and move files accordingly.
   - At the end, it will display the time taken for sorting.

## Customisation
- You can edit the `FOLDERS` dictionary in `main.py` to change which extensions go into which folders.

## Example
Suppose your directory contains:
```
photo.png  song.mp3  video.mp4  doc.txt
```
After running the script, you'll have:
```
images/  audio/  videos/  documents/
```
with the files moved into their respective folders.

## Notes
- Files with unrecognised extensions are moved to the `other` folder.
- The script will not move itself or Python-related files by default.

## future scope: 
- Ability to customise the folders for customised sorting, json based settings control
- Using argparse for fast interface


## License
MIT 