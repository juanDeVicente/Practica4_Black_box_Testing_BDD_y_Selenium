
from selenium import webdriver


def got_to_web():
    driver = webdriver.Firefox()
    driver.get("http://127.0.0.1:8000/")
    return driver

def list_is_not_empty(context):
    try:
        context.find_element_by_id('word0')
        return True
    except:
        return False


def textboxt_empty(context):
    try:
        context.find_element_by_id('username').getValue("")
        return True
    except:
        return False