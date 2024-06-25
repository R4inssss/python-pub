#! python3
#       Just an ATBS example from chapter 12

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException

browser = webdriver.Firefox()
browser.get('https://www.inventwithpython.com')

try:
    elem = browser.find_element_by_class_name(' cover-thumb')
    print('Found <%s> element with that class name!' % (elem.tag_name))
except:
    print('Was not able to find that class name!')
