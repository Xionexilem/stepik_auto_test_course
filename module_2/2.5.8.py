#!/usr/bin/env python3
from math import log, sin
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def calc(x: str) -> str:
    return str(log(abs(12 * sin(int(x)))))


with webdriver.Firefox() as browser:
    browser.get("http://suninjuly.github.io/explicit_wait2.html")

    wait = WebDriverWait(browser, 15)

    wait.until(EC.text_to_be_present_in_element((By.ID, "price"), "100"))

    wait.until(EC.element_to_be_clickable((By.ID, "book"))).click()

    x = wait.until(EC.visibility_of_element_located((By.ID, "input_value"))).text

    answer = calc(x)

    browser.find_element(By.ID, "answer").send_keys(answer)
    browser.find_element(By.ID, "solve").click()

    alert = wait.until(EC.alert_is_present())
    print(alert.text)
    alert.accept()
