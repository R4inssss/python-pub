#! python 3
#       Premade Project on ATBS chapter 10
#       Prompt on files
#       Renames filenames with American MM-DD-YYYY to DD-MM-YYYY format
import os
import shutil
import re

datePattern = re.compile(r"""^(.*?) # We use the carat and the wildcard for all text before the date
    ((0|1)?\d)-                           # We then have one or 2 digits for the months
    ((0|1|2|3)?\d)-                       # one or two digits for the days
    ((19|20)\d\d)                         # four digits for the years
    (.*?)$                                # and then the ending wild card for all text after the date
    """, re.VERBOSE)

for amerFilename in os.listdir('.'):
    mo = datePattern.search(amerFilename)
    if mo is None:
        continue
    beforePart = mo.group(1)
    monthPart = mo.group(2)
    dayPart = mo.group(3)
    yearPart = mo.group(4)
    afterPart = mo.group(5)

    euroFilename = beforePart + dayPart + monthPart + yearPart + afterPart

    absWorkingDir = os.path.abspath('.')
    amerFilename = os.path.join(absWorkingDir, amerFilename)
    euroFilename = os.path.join(absWorkingDir, euroFilename)

    print(f'Renaming "{amerFilename}" to "{euroFilename}"...')
    shutil.move(amerFilename, euroFilename)
