#!/usr/bin/env python3
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from math import log, sin


def calc(x):
    return str(log(abs(12 * sin(int(x)))))


with webdriver.Firefox() as browser:
    wait = WebDriverWait(browser, 10)

    browser.get("http://suninjuly.github.io/redirect_accept.html")

    old_windows = browser.window_handles

    wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button"))).click()

    wait.until(lambda driver: len(driver.window_handles) > len(old_windows))

    new_window = next(
        window for window in browser.window_handles if window not in old_windows
    )
    browser.switch_to.window(new_window)

    x = wait.until(EC.visibility_of_element_located((By.ID, "input_value"))).text

    answer = calc(x)

    browser.find_element(By.ID, "answer").send_keys(answer)
    browser.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

    alert = wait.until(EC.alert_is_present())
    print(alert.text)
    alert.accept()
