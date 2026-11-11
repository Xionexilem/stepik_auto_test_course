import time

from selenium.webdriver.common.by import By


def test_product_page_has_add_to_cart_button(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    browser.get(link)
    time.sleep(30)

    add_to_cart_button = browser.find_element(By.CSS_SELECTOR, "button.btn-add-to-basket")

    print(f"\nAdd to cart button text: {add_to_cart_button.text!r}")
    assert add_to_cart_button.is_displayed(), (
        "Add to cart button is not displayed on the product page"
    )
