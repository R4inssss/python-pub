#! python3
#       cliemailerv2.py - takes an email and string of text from cli
#       uses selenium to log into email and send an email given the email and string from cli


from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


def cliemail():
    browser = webdriver.Firefox()
    browser.get('https://mail.google.com')
    emailElem = browser.find_element(By.ID, 'identifierId')
    emailElem.send_keys('email')
    emailElem.send_keys(Keys.RETURN)


cliemail()

# Userid variable
# Password variable
