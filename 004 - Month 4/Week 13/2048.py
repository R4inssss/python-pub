#! python 3
#       2048.py, a game that plays on https://gabrielecirulli.github.io/2048/
#       all it does is repeat the process of going up,right,down, and left
#       ATBS | Chapter 12 Project 2

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import time


def keys():

    browser = webdriver.Firefox()
    browser.get('https://gabrielecirulli.github.io/2048/')

    while True:
        toUp = WebDriverWait(browser, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, 'body'))
        )
        toUp.send_keys(Keys.UP)
        time.sleep(0.5)

        toRight = WebDriverWait(browser, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, 'body'))
        )
        toRight.send_keys(Keys.RIGHT)
        time.sleep(0.5)

        toDown = WebDriverWait(browser, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, 'body'))
        )
        toDown.send_keys(Keys.DOWN)
        time.sleep(0.5)

        toLeft = WebDriverWait(browser, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, 'body'))
        )
        toLeft.send_keys(Keys.LEFT)
        time.sleep(0.5)

        toScroll = WebDriverWait(browser, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, 'body'))
        )
        toScroll.send_keys(Keys.PAGE_UP)
        time.sleep(0.3)


keys()
