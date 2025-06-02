import pytest
from selene import browser, be, have

@pytest.fixture(scope="module")
def browser_options():
    browser.config.window_width = 1600
    browser.config.window_height = 1200