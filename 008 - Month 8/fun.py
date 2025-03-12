import random

def greet():
    return "Peter is the coolest!"

def joke():
    return "Write a joke here :)"

def fact():
    return "The greeting is a fact"

fun_ctions = [greet, joke, fact]

rand_fun = random.choice(fun_ctions)
print(rand_fun())
