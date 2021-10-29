import pytest
from src.testproject.decorator import report_assertion_errors

from src.testproject.sdk.drivers import webdriver


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


@report_assertion_errors
def test_to_demonstrate_new_features(driver):

    driver.get("https://example.testproject.io/web/")

    driver.find_element_by_css_selector("#name").send_keys("John Smith")
    driver.find_element_by_css_selector("#password").send_keys("12345")
    driver.find_element_by_css_selector("#login").click()

    result = driver.find_element_by_css_selector("#greetings").is_displayed()

    assert result is False
