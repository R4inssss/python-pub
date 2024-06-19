#! python3
#       large_files.py | A program that walks through a tree and searches for large files/folders (100 MB)
#       Then it prints the absolute paths to the screen for the path and its parent folders

import os
from pathlib import Path


def find_files(folder_cwd, size_limit):
    folder_cwd = Path(folder_cwd)
    size_limit_bytes = size_limit * 1024 * 1024

    for foldername, subfolders, files in os.walk(folder_cwd):
        for filename in files:
            file_path = Path(foldername) / filename
            if file_path.is_file() and file_path.stat().st_size > size_limit_bytes:
                print(file_path.resolve())


# We use the .resolve method to convert our path to an absolute path here

folder_cwd = input('Enter folder path: ')
size_limit = 100
# This size limit is in MB, so we convert it in our function above.

find_files(folder_cwd, size_limit)
