#!/usr/bin/env python
# -*- coding: utf-8 -*-
import time
import BDD
from selenium.webdriver.common.keys import Keys


def test_textbox_using_enter():
    context = BDD.got_to_web()
    textbox = context.find_element_by_id("username")
    textbox.send_keys('perezreverte')
    textbox.send_keys(Keys.ENTER)
    time.sleep(4)
    assert BDD.list_is_not_empty(context) == True


def test_username_exists_execute_button():
    context = BDD.got_to_web()
    textbox = context.find_element_by_id("username")
    textbox.send_keys('perezreverte')
    button = context.find_element_by_id("button_execute")
    button.click()
    time.sleep(2)
    assert BDD.list_is_not_empty(context) == True


def test_username_not_exists_execute_button():
    context = BDD.got_to_web()
    textbox = context.find_element_by_id("username")
    textbox.send_keys('noestiejejdlfodjlkhx')
    button = context.find_element_by_id("button_execute")
    button.click()
    assert BDD.list_is_not_empty(context) == False


def test_delete_button_filled_textbox():
    context = BDD.got_to_web()
    textbox = context.find_element_by_id("username")
    textbox.send_keys('perezreverte')
    button = context.find_element_by_id("button_delete")
    button.click()
    time.sleep(2)
    assert BDD.textboxt_empty(context) == True


def test_delete_button_filled_list():
    context = BDD.got_to_web()
    textbox = context.find_element_by_id("username")
    textbox.send_keys('perezreverte')
    button = context.find_element_by_id("button_execute")
    button.click()
    time.sleep(5)
    button2 = context.find_element_by_id("button_delete")
    button2.click()
    time.sleep(2)
    assert BDD.list_is_not_empty(context) == False


def test_empty_list_when_introduce_non_exist_twitter():
    context = BDD.got_to_web()
    textbox = context.find_element_by_id("username")
    textbox.send_keys('perezreverte')
    button = context.find_element_by_id("button_execute")
    button.click()
    time.sleep(5)
    textbox.send_keys('noestiejejdlfodjlkhx')
    button.click()
    time.sleep(2)
    assert BDD.list_is_not_empty(context) == False
