# underscores _ and __

[Source](https://www.youtube.com/watch?v=ALZmCy2u0jQ)

```python
class Test:
	def __init__(self):
		self.foo = 11
		self._bar = 23
		self.__baz = 42

>>> t = Test()
>>> t
>>> <__console__.Test object at 0x10d2bf4a8>
>>> 
```

the underscore in python both have meaning, both by convention and enforced by Python
single underscore is to be treated as private, that is used by convention

double underscore __  is enforced by Python
![[Pasted image 20240523133923.png]]

`foo` and `_bar` are both listed as regular objects

`__baz__` is listed as `_Test__baz` ; name mangling
it does this to protect subclasses

