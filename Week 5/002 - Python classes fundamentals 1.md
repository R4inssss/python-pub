Classes are used to define an object (describe an object)
It describes what the object does, what it resembles, etc
From: https://www.youtube.com/watch?v=rJzjDszODTI


First, init and self; From: https://stackoverflow.com/questions/625083/what-do-init-and-self-do-in-python

```
the `self` variable represents the instance of the object itself. Most object-oriented languages pass this as a hidden parameter to the methods defined on an object; Python does not. You have to declare it explicitly
```

Self = 'this instance of the class'
from: https://www.youtube.com/watch?v=_mjZjpOmN0k


So, it's declaring itself. Nice and understandable
```
The `__init__` method is roughly what represents a constructor in Python. When you call `A()` Python creates an object for you, and passes it as the first parameter to the `__init__` method. Any additional parameters (e.g., `A(24, 'Hello')`) will also get passed as arguments--in this case causing an exception to be raised, since the constructor isn't expecting them.
```
WTF IS A CONSTUCTOR???
https://www.geeksforgeeks.org/constructors-in-python/
OK, so [[constructors]] are used for instantiating (representing an initiation) an object.
==The task of constructors is to initialize(assign values) to the data members of the class when an object of the class is created==. In Python the __init__() method is called the constructor and is always called when an object is created.

**Types of constructors :** 

- **default constructor:** The default constructor is a simple constructor which doesn’t accept any arguments. Its definition has only one argument which is a reference to the instance being constructed.
- **parameterized constructor:** constructor with parameters is known as parameterized constructor. The parameterized constructor takes its first argument as a reference to the instance being constructed known as self and the rest of the arguments are provided by the programmer.
Default:
```
`class` `GeekforGeeks:`

    `# default constructor`

    `def` `__init__(``self``):`

        `self``.geek` `=` `"GeekforGeeks"`

    `# a method for printing data members`

    `def` `print_Geek(``self``):`

        `print``(``self``.geek)`

`# creating object of the class`

`obj` `=` `GeekforGeeks()`

`# calling the instance method using the object obj`

`obj.print_Geek()`
```

Parameterized:
```
`class` `Addition:`

    `first` `=` `0`

    `second` `=` `0`

    `answer` `=` `0`

    `# parameterized constructor`

    `def` `__init__(``self``, f, s):`

        `self``.first` `=` `f`

        `self``.second` `=` `s`

    `def` `display(``self``):`

        `print``(``"First number = "` `+` `str``(``self``.first))`

        `print``(``"Second number = "` `+` `str``(``self``.second))`

        `print``(``"Addition of two numbers = "` `+` `str``(``self``.answer))`

    `def` `calculate(``self``):`

        `self``.answer` `=` `self``.first` `+` `self``.second`

`# creating object of the class`

`# this will invoke parameterized constructor`

`obj1` `=` `Addition(``1000``,` `2000``)`

`# creating second object of same class`

`obj2` `=` `Addition(``10``,` `20``)`

`# perform Addition on obj1`

`obj1.calculate()`

`# perform Addition on obj2`

`obj2.calculate()`

`# display result of obj1`

`obj1.display()`

`# display result of obj2`

`obj2.display()`
```

