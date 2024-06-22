#! python3
#       selectiveCopy.py | a program that walks through a tree
#       searches for specific file extensions, and copies these files into a new folder
import os
import shutil
from pathlib import Path


def selective_copy(source_folder, destination_folder, extensions):
    source_folder = Path(source_folder)
    destination_folder = Path(destination_folder)
    destination_folder.mkdir(parents=True, exist_ok=True)

    counter = 1

    for foldername, subfolders, filenames in os.walk(source_folder):
        for filename in filenames:
            if any(filename.endswith(ext) for ext in extensions):
                source_file = Path(foldername) / filename
                name, ext = os.path.splitext(filename)

                target_file = destination_folder / f"{name}_{counter}{ext}"

                shutil.copy(source_file, target_file)
                print(f'Copied {source_file} to {target_file}')
                counter += 1


source_folder = Path.cwd()
target_folder = source_folder / 'photo_backup'
extensions = ['.jpg', '.jpeg', '.png']

selective_copy(source_folder, target_folder, extensions)

# The prompt ask us to walk through a folder tree and search for files with certain extensions
# Then copy these files to wherever we want, in this instance I want it to be in CWD.
