import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import *


class TestLogin:
    def test_successful_login(self, driver):
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

        user_avatar = driver.find_element(*USER_AVATAR)
        user_name = driver.find_element(*USER_NAME)

        assert user_avatar.is_displayed()
        assert user_name.is_displayed()
        assert "User" in user_name.text