# DHKE example 1


def peekaboo(g, p, A):
  a = 1
  while True:
    if pow(g, a, p) == A:
      return a
    a += 1
    if a > p:
      break
  return None

# Given:
g=2
p=499
A=16



peekaboohoo = peekaboo(g, p, A)
print(f'Your key: {peekaboohoo}')



# A=(g**a)%p has been intercepted on the wire!
# What is the secret component, a?
# Given that g = 2 p = 499 and A = 16
# given the forumala A = G^a (that's where the ** comes from)
# first we would need to make a function that uses the secret key, we would then use the variables given as parameters for our function
# then, we need to make our variables = A, we can do this by using the power of function in python
# to do this properly we need to lay it out as (base, exponent, and modulus) https://stackoverflow.com/questions/32738637/calculate-mod-using-pow-function-python
# fun stuff
# where a = 1, and the iteration = the secret eky
# we increment the exponent by one recursively
# if a > p end the program
# else it continues