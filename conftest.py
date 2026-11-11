import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    parser.addoption(
        "--language",
        action="store",
        default="en",
        help="Language of the browser interface, for example: es, fr, ru",
    )


@pytest.fixture(scope="function")
def browser(request):
    language = request.config.getoption("--language")

    options = Options()
    options.add_experimental_option("prefs", {"intl.accept_languages": language})

    print(f"\nStart Chrome browser with interface language '{language}'...")
    browser = webdriver.Chrome(options=options)
    yield browser
    print("\nQuit browser...")
    browser.quit()
