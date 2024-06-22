#! python3
#       backupToZip.py and ATBS project
#       chapter 10 project 2 | copies an entire folder and its contents into a zipfile whose filename increments

import zipfile
import os


def backupToZip(folder):
    folder = os.path.abspath(folder)
    number = 1
    while True:
        zipfilename = os.path.basename(folder) + '_' + str(number) + '.zip'
        if not os.path.exists(zipfilename):
            break
        number = number + 1

    print(f'Creating {zipfilename}...')
    backupzip = zipfile.ZipFile(zipfilename, 'w')

    for foldername, subfolders, filenames in os.walk(folder):
        print(f'Adding files in {foldername}')
        backupzip.write(foldername)

        for filename in filenames:
            newbase = os.path.basename(folder) + '_'
            if filename.startswith(newbase) and filename.endswith('.zip'):
                continue
            backupzip.write(os.path.join(foldername, filename))
    backupzip.close()
    print(f'Done!')




backupToZip('C:\\delicious')
