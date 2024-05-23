I really wanted to use shelves and opening it within my classes
Well, I know how to do shelves
I knew how to do shelve.open()
i knew how to shelve.close()
and I know as statements
but, that looks ugly!

Insert the with statements!
[We do googlin](https://www.freecodecamp.org/news/with-open-in-python-with-statement-syntax-example/)

Well, it turns out open has a lot cooler things with it instead of just w/r/a
open takes up to 3 parameters, the filename, the mode, and the encoding which we have all done before.


The [[with]] statement!
The `with` statement works with the `open()` function to open a file.
And closes it as well!
```python
with open("hello.txt") as my_file:
    print(my_file.read())

# Output : 
# Hello world
# I hope you're doing well today
# This is a text file
```


the `with` statement closes the file for you without you telling it to!!!!!!!
 no shelve.close??!?
Beautiful


This is because the `with` statement calls 2 built-in methods behind the scene – `__enter()__` and `__exit()__`. See source 2 context managers for more information.

# Source 2 - youtube
Wait wait wait, lets go review some context managers: [with statement source 2](https://www.youtube.com/watch?v=iba-I4CrmyA)

To demystify the with statement
```python
with open('hello.txt', 'w') as f:
	f.write('hello world!')
```
is equivalent to:
```python
f = open('hello.txt', 'w')
try:
	f.write('hello, world!')
finally:
	f.close()
```

## now Context Mangers!
[[context managers]] - contract that your object follows so that it can be used with the with statement
enter and exit method
```python
# Context Mangers
class ManagedFile:
	def __init__(self,name):
		self.name = name
	def __enter__(self):
		self.file = open(self.name, 'w')
		return self.file
	def __exit__(self, exc_type, exc_val, exc_tb):
		if self.file:
			self.file.close()
```
the first [[constructor]]  (remember from before) assigns the name (self.name = name) and remembers the name for the file we want to create
the second acquires the resources and opens the file to write mode
the exit method releases the resources and closes the file. 

example:
```python
mf = ManagedFile('hello.txt')
mf
<error>
# but if you do the following
with mf as the_file:
	the_file.write('hello.txt)
>>> 9
```
behind the scenes, it does the first example of context managers in the second version

