# English to Pig Latin
print('Enter the English message to translate into Pig Latin:')
message = input()

VOWELS = ('a', 'e', 'i', 'o', 'u', 'y')

pigLatin = [] # A list of the words in Pig Latin.
for word in message.split():
    # Separate the non-letters at the start of this word:
    prefixNonLetters = ''
    while len(word) > 0 and not word[0].isalpha():
        prefixNonLetters += word[0]
        word = word[1:]
    if len(word) == 0:
        pigLatin.append(prefixNonLetters)
        continue

    # Separate the non-letters at the end of this word:
    suffixNonLetters = ''
    while not word[-1].isalpha():
        suffixNonLetters = word[-1] + suffixNonLetters
        word = word[:-1]

    # Remember if the word was in uppercase or title case.
    wasUpper = word.isupper()
    wasTitle = word.istitle()

    word = word.lower() # Make the word lowercase for translation.

    # Separate the consonants at the start of this word:
    prefixConsonants = ''
    while len(word) > 0 and not word[0] in VOWELS:
        prefixConsonants += word[0]
        word = word[1:]

    # Add the Pig Latin ending to the word:
    if prefixConsonants != '':
        word += prefixConsonants + 'ay'
    else:
        word += 'yay'

    # Set the word back to uppercase or title case:
    if wasUpper:
        word = word.upper()
    if wasTitle:
        word = word.title()

    # Add the non-letters back to the start or end of the word.
    pigLatin.append(prefixNonLetters + word + suffixNonLetters)

# Join all the words back together into a single string:
print(' '.join(pigLatin))



# first, we print a string of text
# we then create the variable message, which is the input 
# then we assign the variable vowels to a list of vowels
# We then create an empty list for pigLatin
# we then create a for loop with the variable word, which iterates through our first variable message
# using the split method
# our first if statements is 
# first assigning a variable as an empty string
# then creating a while loop, for the lenth of word greater than 0 and the first letter
# in word is not a number
# then the variable is now equal to the word + 1
# it then assigns word to the remaining sections of the string using word[1:]
# and after, it appends list together using the variable prefixNonLetters
# and uses the continue statement
# the rest of it is just iteraing through various isx methods, moving it based on the position of the 
# word
# and adding on the variables
# and strings 
# at the end, it appends the variables together
# and prints our piglatin using the .join method