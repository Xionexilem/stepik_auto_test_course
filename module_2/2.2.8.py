#!/usr/bin/env python3
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoAlertPresentException
import os, time

MAIN_LINK = "http://suninjuly.github.io/file_input.html"
browser = webdriver.Firefox()
wait = WebDriverWait(browser, 10)

try:
    browser.get(MAIN_LINK)

    browser.find_element(By.CSS_SELECTOR, "input[name='firstname']").send_keys("Ivan")
    browser.find_element(By.CSS_SELECTOR, "input[name='lastname']").send_keys("Petrov")
    browser.find_element(By.CSS_SELECTOR, "input[name='email']").send_keys(
        "example@gmail.com"
    )

    file_path = os.path.abspath("2.2.8.txt")
    print("FILE EXISTS:", os.path.exists(file_path), "->", file_path)
    assert os.path.exists(file_path), "файла нет!"

    browser.find_element(By.CSS_SELECTOR, "#file").send_keys(file_path)

    val = browser.find_element(By.CSS_SELECTOR, "#file").get_attribute("value")
    print("FILE INPUT VALUE:", val)

    btn = browser.find_element(By.CSS_SELECTOR, "button.btn")
    print("BUTTON TEXT:", btn.text, "| ENABLED:", btn.is_enabled())

    browser.save_screenshot("before_click.png")

    btn.click()
    print("Клик сделан")

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
    time.sleep(10)
    browser.quit()
