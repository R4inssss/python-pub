#! python3
#       An ATBS premade project | Combines all the PDFs in your current working directory
#       ATBS Chapter 15

import PyPDF2
import os

# Finds filenames that end with a .pdf extension, then appends it to our list
pdfFiles = []
for filename in os.listdir('.'):
    if filename.endswith('.pdf'):
        pdfFiles.append(filename)

pdfFiles.sort(key=str.lower)

pdfWriter = PyPDF2.PdfFileWriter()

# For each of our files inside the list, it opens the list in read binary mode.
for filename in pdfFiles:
    pdfFileObj = open(filename, 'rb')
    pdfReader = PyPDF2.PdfFileReader(pdfFileObj)  # After, we iterate through our new object using PdfFileReader method

    # Loop through all the pages (except the first) and add them.
    for pageNum in range(1, pdfReader.numPages):
        pageObj = pdfReader.getPage(pageNum)
        pdfWriter.addPage(pageObj)

pdfOutput = open('allminutes.pdf', 'wb')
pdfWriter.write(pdfOutput)
pdfOutput.close()
