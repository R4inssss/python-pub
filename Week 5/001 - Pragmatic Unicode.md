
https://www.youtube.com/watch?v=sgHbC6udIqc

UTF - 8 is the king of encoding :D
ASCII characters are still in one byte

Python 2:
string = str
unicode = unicode - this stores codepoints

.encode() and .decode()
unicode.encode() -> bytes
bytes.decode() -> unicode

python 2 is funny, decoding/encoding errors

There is both bytes and unicode

Python 3:
str: a sequence of code points (unicode)
bytes: a sequence of bytes

no coercion -> python 3 will not translate/convert unicode to ascii/vice versa

IT IS EXPLICIT, UNICODE AND BYTES IS DEAL WITH BOTH!

default r mode = unicode string
rb = byte string
![[Pasted image 20240501200810.png]]

![[Pasted image 20240501200928.png]]

![[Pasted image 20240501201143.png]]

