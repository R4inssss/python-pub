#! python3
#       cliemailerv2.py - takes an email and string of text from cli
#       uses selenium to log into email and send an email given the email and string from cli


from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import getpass
import time


def cliemail():
    email = input('Enter your email: ')
    password = getpass.getpass('Enter your password: ')
    recipient = input('Enter recipient email: ')
    subject = input('Enter your subject: ')
    body = input('Enter your message: ')
    browser = webdriver.Firefox()
    browser.get('https://mail.google.com')
    i = 0  # subject counter

    try:
        # Email
        emailElem = browser.find_element(By.ID, 'identifierId')
        emailElem.send_keys(email)
        emailElem.send_keys(Keys.RETURN)

        # Password
        passwordElem = WebDriverWait(browser, 10).until(
            EC.visibility_of_element_located((By.NAME, 'Passwd'))
        )
        passwordElem.send_keys(password)
        passwordElem.send_keys(Keys.RETURN)

        while i <= 10:
            # Find Compose Button
            composeElem = WebDriverWait(browser, 10).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, '.T-I-KE'))
            )

            composeElem.send_keys(Keys.RETURN)

            # Find email field
            toElem = WebDriverWait(browser, 10).until(
                EC.element_to_be_clickable((By.XPATH, '//input[@aria-label="To recipients"]'))
            )
            toElem.send_keys(recipient)

            # Find subject field
            toSub = WebDriverWait(browser, 10).until(
                EC.element_to_be_clickable((By.NAME, 'subjectbox'))
            )
            toSub.send_keys(subject + str(i))

            # Find Message body
            toBody = WebDriverWait(browser, 10).until(
                EC.element_to_be_clickable((By.XPATH, '//div[@aria-label="Message Body"]'))
            )
            toBody.send_keys(body)

            # Find send button

            toSend = WebDriverWait(browser, 10).until(
                EC.element_to_be_clickable((By.XPATH, '//div[@role="button" and text()="Send"]'))
            )
            toSend.send_keys(Keys.RETURN)

            time.sleep(5)  # change int here if you want faster loops

            i += 1  # moved for clarity, incremental counter of loop iterated through subject field

    except Exception as e:
        print(f'Error: {e}')
    finally:
        browser.quit()
        print('Browser closed, your spam has been executed!')


cliemail()

# Debug Code
# def test_pass():
#     password = getpass.getpass('Enter your password: ')
#     print(password)
#     print(type(password))
#
# test_pass()

# Userid variable
# Password variable
