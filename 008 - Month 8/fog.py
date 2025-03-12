def double(x):
    return x * 2

def square(x):
    return x ** 2

def increment(x):
    return x + 1 # No x++!

def fog(f1, f2, x):
    return f2(f1(x))

ask = int(input(">>> "))

result = fog(double, square, ask)
print(result)
