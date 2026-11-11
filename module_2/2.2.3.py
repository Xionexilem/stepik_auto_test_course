#!/usr/bin/env python3
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

LINK = "https://suninjuly.github.io/selects1.html"

browser = webdriver.Firefox()

try:
    browser.get(LINK)

    num1: int = int(browser.find_element(By.ID, "num1").text)
    num2: int = int(browser.find_element(By.ID, "num2").text)
    sum: int = num1 + num2

    option = browser.find_element(By.CSS_SELECTOR, f"#dropdown > option[value='{sum}']")
    option.click()

    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()


finally:
    time.sleep(30)
    browser.quit()
