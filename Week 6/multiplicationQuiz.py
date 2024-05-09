# Project 2 of Chapter 8 ; try/except/else/finally demonstration

import pyinputplus as pyip
import random, time


numberofQuestions = 10
correctAnswers = 0

for questionNumber in range(numberofQuestions):
    # our 2 random numbers
    # here, we use the range of our variable number of questions to dictate how many times the\
    # quiz is iterated
    num1 = random.randint(0,9)
    num2 = random.randint(0,9)
    # here, we iterate our variables using the %s, which allows us to incorporate a given string
    # within another string, but in this case they're numbers
    # in this case, we're using the 3 varables to iterate exactly as said down below
    prompt = '#%s: %s x %s = ' % (questionNumber, num1, num2)
    try:
    # our first run in with the try clause/block! here, it tries to do the following
    # Right answers are handled by allowRegexes.
    # Wrong answers are handled by blockRegexes, with a custom message.
        pyip.inputStr(prompt, allowRegexes=['^%s$' % (num1 * num2)],
                                blockRegexes=[('.*', 'Incorrect!')],
                                timeout=8, limit=3)
    # here, we are uinsg the inputstring method and iterating our prompt variable
    # with the pyip methods of regex to parse through our variable.
    # really cool stuff, the ^ and % characters ensure that the answer begins and end with the correct number
    # The first string in the tuple is a regex that matches every possible string
    # And if the input response doesn't match the correct answer, the program will pass the blockRegexes variable
    # then, there are parameters that give 8 seconds per answer, as well as 3 attempts.

    except pyip.TimeoutException:
        print('Out of time!')
    except pyip.RetryLimitException:
        print('Out of tries!')
    # our except block
    # funny enough, I did not include this at first and was VERY confused in why
    # our except block runs when the try block fails to pass
    else:
            # This block runs if no exceptions were raised in the try block.
        print('Correct!')
        correctAnswers += 1
    # all else, it passes the string correct
    # and raises the correct answers by 1.
    #    finally:
    #        print('Try, except, else, finally demonstration')



    time.sleep(0.5) # Brief pause to let user see the result.
print('Score: %s / %s' % (correctAnswers, numberofQuestions))
    # using %s as place holders for correctAnswers and numberofQuestions