#! python3
#       cliemailerv2.py - takes an email and string of text from cli
#       uses selenium to log into email and send an email given the email and string from cli


from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import getpass


def cliemail():
    email = input('Enter your email: ')
    password = getpass.getpass('Enter your password: ')
    browser = webdriver.Firefox()
    browser.get('https://mail.google.com')

    emailElem = browser.find_element(By.ID, 'identifierId')
    emailElem.send_keys(email)
    emailElem.send_keys(Keys.RETURN)

    passwordElem = WebDriverWait(browser, 10).until(
        EC.visibility_of_element_located((By.NAME, 'Passwd'))
    )
    passwordElem.send_keys(password)
    passwordElem.send_keys(Keys.RETURN)


# Fine Compose Button
# Find email field
# Find subject field
# Find Message body
# Find send button

cliemail()

# Debug Code
# def test_pass():
#     password = getpass.getpass('Enter your password: ')
#     print(password)
#     print(type(password))
#
#
# test_pass()

# Userid variable
# Password variable
