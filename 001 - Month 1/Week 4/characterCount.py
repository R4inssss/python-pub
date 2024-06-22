import pprint

message = 'It was a bright cold day in April, and the clocks were striking thirteen.'

count = {}

for character in message:
    count.setdefault(character, 0)
    count[character] = count[character] + 1


pprint.pprint(count)

# here, we declare the variable message as a string of text
# then we create a dictionary named count
# we use a for loop to do the following:
# we use a new variable name character, or parameter
# we the method setdefault, and place each key is in the count dictionary
# the default value of 0, so there are no errors when count[character] + 1 is invoked
# Then, each character is iterated and incrementally increased by 1 per instance.
# we then added the pprint module
# And we used pprint.pprint 