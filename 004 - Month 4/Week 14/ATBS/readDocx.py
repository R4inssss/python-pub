#! python3
#       readDocx.py | reads documents from a docx file using python cli
#       ATBS Chapter 15 | An ATBS premade script

import docx


def getText(filename):
    doc = docx.Document(filename)
    fulltext = []
    for paragraph in doc.paragraphs:
        fulltext.append(paragraph.text)
    return '\n'.join(fulltext)
