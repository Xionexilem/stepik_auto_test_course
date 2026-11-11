#!/usr/bin/env python3
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import math, time

MAIN_LINK = "http://suninjuly.github.io/alert_accept.html"

browser = webdriver.Firefox()

wait = WebDriverWait(browser, 10)


def calc(x: str):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    browser.get(MAIN_LINK)

    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    confirm = browser.switch_to.alert
    confirm.accept()

    time.sleep(2)

    x_element = browser.find_element(By.CSS_SELECTOR, "#input_value")
    x = x_element.text
    y = calc(x)
    print(y)

    input = browser.find_element(By.CSS_SELECTOR, "#answer")
    input.send_keys(y)

    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    try:
        alert = wait.until(EC.alert_is_present())
        print("ALERT TEXT:", alert.text)
        alert.accept()
    except TimeoutException:
        print("ALERT НЕ ПОЯВИЛСЯ за 10 сек")
        print("URL:", browser.current_url)
        print("TITLE:", browser.title)
        print(browser.page_source[:2000])
        browser.save_screenshot("after_click.png")

finally:
    time.sleep(30)
    browser.quit()
