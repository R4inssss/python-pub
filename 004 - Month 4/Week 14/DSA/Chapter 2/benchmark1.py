#! python 3
#       Expanded on chapter 2.2's topic a little by doing my own variation of ∑(i) = (n(n+1))/2

import time


def sum_of_n_3(n):
    start = time.time()
    result = (n * (n + 1)) / 2
    end = time.time()
    return result, end - start


for i in range(5000):
    s, t = sum_of_n_3(100000)
    print("Sum is %d required %10.7f seconds" % (s, t))


# Results:
# Sum is 5000050000 required  0.0000000 seconds
# Sum is 5000050000 required  0.0000000 seconds
# Sum is 5000050000 required  0.0000000 seconds
# Sum is 5000050000 required  0.0000000 seconds
# Sum is 5000050000 required  0.0000000 seconds
# Sum is 5000050000 required  0.0000000 seconds
# Sum is 5000050000 required  0.0000000 seconds
# Sum is 5000050000 required  0.0000000 seconds
# Sum is 5000050000 required  0.0000000 seconds
# Sum is 5000050000 required  0.0000000 seconds
# Sum is 5000050000 required  0.0000000 seconds
# Sum is 5000050000 required  0.0000000 seconds
# Sum is 5000050000 required  0.0000000 seconds
