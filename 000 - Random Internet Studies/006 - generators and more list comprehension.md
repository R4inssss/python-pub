# Source 1
https://stackoverflow.com/questions/1756096/understanding-generators-in-python

A [[generator]] is simply a function which returns an object on which you can call `next`, such that for every call it returns some value, until it raises a `StopIteration` exception, signaling that all values have been generated. Such an object is called an _iterator_.

Normal functions return a single value using `return`, just like in Java. In Python, however, there is an alternative, called `yield`. Using `yield` anywhere in a function makes it a generator. Observe this code:

```python
>>> def myGen(n):
...     yield n
...     yield n + 1
... 
>>> g = myGen(6)
>>> next(g)
6
>>> next(g)
7
>>> next(g)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
StopIteration
```

As you can see, `myGen(n)` is a function which yields `n` and `n + 1`. Every call to [`next`](http://docs.python.org/3/library/functions.html#next) yields a single value, until all values have been yielded. `for` loops call `next` in the background, thus:

```python
>>> for n in myGen(6):
...     print(n)
... 
6
7
```

Likewise there are [_generator expressions_](http://www.python.org/dev/peps/pep-0289/), which provide a means to succinctly describe certain common types of generators:

```python
>>> g = (n for n in range(3, 5))
>>> next(g)
3
>>> next(g)
4
>>> next(g)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
StopIteration
```

Note that generator expressions are much like [_list comprehensions_](http://docs.python.org/3/tutorial/datastructures.html#list-comprehensions):

```python
>>> lc = [n for n in range(3, 5)]
>>> lc
[3, 4]
```

Observe that a generator object is generated _once_, but its code is _not_ run all at once. Only calls to `next` actually execute (part of) the code. Execution of the code in a generator stops once a `yield` statement has been reached, upon which it returns a value. The next call to `next` then causes execution to continue in the state in which the generator was left after the last `yield`. This is a fundamental difference with regular functions: those always start execution at the "top" and discard their state upon returning a value.

There are more things to be said about this subject. It is e.g. possible to `send` data back into a generator ([reference](http://docs.python.org/3/reference/expressions.html#yield-expressions)). But that is something I suggest you do not look into until you understand the basic concept of a generator.

Now you may ask: why use generators? There are a couple of good reasons:

- Certain concepts can be described much more succinctly using generators.
- Instead of creating a [[function]] which returns a list of values, one can write a generator which generates the values on the fly. This means that no list needs to be constructed, meaning that the resulting code is more memory efficient. In this way one can even describe data streams which would simply be too large to fit in memory.
- Generators allow for a natural way to describe _infinite_ streams. Consider for example the [Fibonacci numbers](http://en.wikipedia.org/wiki/Fibonacci_number):
    
    ```python
    >>> def fib():
    ...     a, b = 0, 1
    ...     while True:
    ...         yield a
    ...         a, b = b, a + b
    ... 
    >>> import itertools
    >>> list(itertools.islice(fib(), 10))
    [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
    ```
    
    This code uses [`itertools.islice`](http://docs.python.org/3/library/itertools.html#itertools.islice) to take a finite number of elements from an infinite stream. You are advised to have a good look at the functions in the [`itertools`](http://docs.python.org/3/library/itertools.html) module, as they are essential tools for writing advanced generators with great ease.
    

---

  † **About Python <=2.6:** in the above examples `next` is a function which calls the method `__next__` on the given object. In Python <=2.6 one uses a slightly different technique, namely `o.next()` instead of `next(o)`. Python 2.7 has `next()` call `.next` so you need not use the following in 2.7:

```python
>>> g = (n for n in range(3, 5))
>>> g.next()
3
```


# Source 2 
https://www.youtube.com/watch?v=bD05uGo_sVI

using yield instead of returning the result of a list (array) given a set of integers
when using a list and iterating it, it would look like:

```python
def square_numbers(nums):
	result = []
	for i in nums:
		result.append(i*i)
	return result

my_nums = square_numbers([1,2,3,4,5])
print my_nums
	
```
instead of doing all this, you can do:
```python
def square_numbers(nums):
	for i in nums:
		yield (i*i)
my_nums = square_numbers([1,2,3,4,5])
print my_nums

```
This will return a "generator object"
if doing next(my_nums) to pass through the operator and initial sequence

```python
def square_numbers(nums):
	for i in nums:
		yield (i*i)
my_nums = square_numbers([1,2,3,4,5])
print next(my_nums)

```

this would show the results of the squared numbers for each instance.

To print out all values, you would do:

```python
def square_numbers(nums):
	for i in nums:
		yield (i*i)
my_nums = square_numbers([1,2,3,4,5])
for num in my_nums:
	print num
```

The for loop knows when to stop.
