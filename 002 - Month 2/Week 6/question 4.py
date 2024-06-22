# Question 4 in chapter 8 practice questions

import pyinputplus as pyip
import sys



while True:
    try:
        number = pyip.inputInt('Input numbers between 0-99: ', min = 0, max = 99)
    except ValueError as e:
        print(f'Bad input \n {e}')
    except KeyError as e:
        print(e)
    except Exception as e:
        print(e)
    else:
        print(f'Your number is: {number + 3}')
    #   sys.exit()

