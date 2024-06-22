#! python3
#       selectiveCopy.py | a program that walks through a tree
#       searches for specific file extensions, and copies these files into a new folder
import os
import shutil
from pathlib import Path


def copying(source_folder, destination_folder, extensions):
    source_folder = Path(source_folder)
    destination_folder = Path(destination_folder)
    extensions = Path(extensions)

    counter = 1

    for foldername, subfolders, filenames in os.walk(source_folder):
        for filename in filenames:
            if any(filename.endswith(ext) for ext in extensions):
                source_file = Path(foldername) / filename
                shutil.copy(source_file, destination_folder)
                print(f'Copied {source_file} to {destination_folder}')


source_folder = Path.cwd()
destination_folder = source_folder.parent / 'backup'
extensions = ['jpg', 'jpeg', 'png']


# The prompt ask us to walk through a folder tree and search for files with certain extensions
# Then copy these files to wherever we want, in this instance I want it to be in CWD.
