#!/usr/bin/env python3
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

LINK = "https://suninjuly.github.io/math.html"

browser = webdriver.Firefox()


def calc(x: str):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    browser.get(LINK)

    x_element = browser.find_element(By.CSS_SELECTOR, "#input_value")
    x = x_element.text
    y = calc(x)

    input1 = browser.find_element(By.TAG_NAME, "input")
    input1.send_keys(y)
    option1 = browser.find_element(By.CSS_SELECTOR, "[for='robotCheckbox']")
    option1.click()
    option2 = browser.find_element(By.CSS_SELECTOR, "[for='robotsRule']")
    option2.click()
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:
    time.sleep(30)
    browser.quit()
