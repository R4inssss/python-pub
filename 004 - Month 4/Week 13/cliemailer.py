#! python3
#       cliemailerv2.py - takes an email and string of text from cli
#       uses selenium to log into email and send an email given the email and string from cli


from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import getpass


def cliemail():
    email = input('Enter your email: ')
    password = getpass.getpass('Enter your password: ')
    browser = webdriver.Firefox()
    browser.get('https://mail.google.com')
    emailElem = browser.find_element(By.ID, 'identifierId')
    emailElem.send_keys(email)
    emailElem.send_keys(Keys.RETURN)
    email.send_keys(password)
    print(type(password))
    emailElem.send_keys(Keys.RETURN)


# cliemail()


def test_pass():
    password = getpass.getpass('Enter your password: ')
    print(password)
    print(type(password))


test_pass()

# Userid variable
# Password variable
