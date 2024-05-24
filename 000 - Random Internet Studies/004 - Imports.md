Source 1:
https://realpython.com/python-import/#:~:text=In%20Python%2C%20you%20use%20the,while%20keeping%20your%20projects%20maintainable.

Importing can be used explicityly
ie:
```
from (module) import (thingy)
```

Importing can be renamed to something shorter:
```
import xxxxxxxxxxxxxx as x
```
allowing you to do
```
x.method()
```
instead of:
```
xxxxxxxxxx.method()
```


you can use the dir(module/package) command to view the contents of a namespace.
```
dir(module)
```
Term for [[modules]]:
An object that serves as an organizational unit of Python code. Modules have a namespace containing arbitrary Python objects. Modules are loaded into Python by the process of importing

Term for [[packages]]:
A Python module which can contain submodules or recursively, subpackages. Technically, a package is a Python module with an `__path__` attribute.


# Absolute and relative imports:

(.) from:

```
from . import xxxxx
```
refers to a relative import, which can be read as "From the current package import xxxxx".

There’s an equivalent **absolute import** statement in which you explicitly name the current package:
```
from world import africa
```

