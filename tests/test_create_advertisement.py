import time
import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from locators import *

class TestAdvertisement:
    def test_create_ad_unauthenticated(self, driver):
        create_ad_btn = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(CREATE_AD_BUTTON)
        )
        create_ad_btn.click()

        auth_modal = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(AUTH_REQUIRED_MODAL)
        )

        assert auth_modal.is_displayed()
        assert "Чтобы разместить объявление, авторизуйтесь" in auth_modal.text

    def test_create_ad_authenticated(self, driver):
        login_btn = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(LOGIN_REG_BUTTON)
        )
        login_btn.click()

        no_account_btn = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(NO_ACCOUNT_BUTTON)
        )
        no_account_btn.click()

        timestamp = int(time.time())
        email = f"ad_test_user_{timestamp}@example.com"
        password = "TestPassword123"

        email_field = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(REG_EMAIL_INPUT)
        )
        email_field.send_keys(email)

        password_field = driver.find_element(*REG_PASSWORD_INPUT)
        password_field.send_keys(password)

        confirm_password_field = driver.find_element(*REG_CONFIRM_PASSWORD_INPUT)
        confirm_password_field.send_keys(password)

        create_account_btn = driver.find_element(*CREATE_ACCOUNT_BUTTON)
        create_account_btn.click()

        WebDriverWait(driver, 15).until(
            EC.presence_of_element_located(USER_AVATAR)
        )

        create_ad_btn = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(CREATE_AD_BUTTON)
        )
        create_ad_btn.click()

        WebDriverWait(driver, 10).until(
            EC.any_of(
                EC.presence_of_element_located(AD_TITLE_INPUT),
                lambda d: "create" in d.current_url.lower() or 
                         "new" in d.current_url.lower() or 
                         "add" in d.current_url.lower()
            )
        )

        try:
            title_field = WebDriverWait(driver, 5).until(
                EC.presence_of_element_located(AD_TITLE_INPUT)
            )
            assert title_field.is_displayed()
        except:
            current_url = driver.current_url
            assert "create" in current_url or "new" in current_url or "add" in current_url