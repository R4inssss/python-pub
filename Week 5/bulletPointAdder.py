#! python3

# bulletPointAdder.py - Adds Wikipedia bullet points to the start of each line of text on the clipboard.



import pyperclip

text = pyperclip.paste()


lines = text.split('\n')
for i in range(len(lines)):    
    lines[i] = '* ' + lines[i] 
text = '\n'.join(lines)
pyperclip.copy(text)


# So, we again are using the pyperclip module
# we declare the variable text == pyperclip.paste() method
# we then make lines == text.split('\n') where we use the split method, and add \n for new line
# we then iterate through lines, using the range of the length of each line
# for every line, we ad a * in front of it
# we then use the .join method, joining the data in lines and assigning it to the text variable
# after, we use the .copy method to copy the iteration given by the text variable