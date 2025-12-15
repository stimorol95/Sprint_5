import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import *

class TestLogout:
    def test_successful_logout(self, driver):
        login_btn = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(LOGIN_REG_BUTTON)
        )
        login_btn.click()

        test_email = "test@example.com"
        test_password = "password123"

        email_field = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(AUTH_EMAIL_INPUT)
        )
        email_field.send_keys(test_email)

        password_field = driver.find_element(*AUTH_PASSWORD_INPUT)
        password_field.send_keys(test_password)

        login_submit_btn = driver.find_element(*LOGIN_BUTTON)
        login_submit_btn.click()

        WebDriverWait(driver, 15).until(
            EC.presence_of_element_located(USER_AVATAR)
        )

        logout_btn = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(LOGOUT_BUTTON)
        )
        logout_btn.click()

        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(LOGIN_REG_BUTTON)
        )

        login_button_after_logout = driver.find_element(*LOGIN_REG_BUTTON)
        assert login_button_after_logout.is_displayed()

        avatar_elements = driver.find_elements(*USER_AVATAR)
        name_elements = driver.find_elements(*USER_NAME)
        assert len([e for e in avatar_elements if e.is_displayed()]) == 0
        assert len([e for e in name_elements if e.is_displayed()]) == 0
