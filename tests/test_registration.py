import time
import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from locators import *

class TestRegistration:
    def test_successful_registration(self, driver):
        login_btn = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(LOGIN_REG_BUTTON)
        )
        login_btn.click()

        no_account_btn = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(NO_ACCOUNT_BUTTON)
        )
        no_account_btn.click()

        timestamp = int(time.time())
        email = f"test_user_{timestamp}@example.com"
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

        user_avatar = driver.find_element(*USER_AVATAR)
        user_name = driver.find_element(*USER_NAME)

        assert user_avatar.is_displayed()
        assert user_name.is_displayed()
        assert "User" in user_name.text

    def test_registration_invalid_email(self, driver):
        login_btn = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(LOGIN_REG_BUTTON)
        )
        login_btn.click()

        no_account_btn = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(NO_ACCOUNT_BUTTON)
        )
        no_account_btn.click()

        email_field = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(REG_EMAIL_INPUT)
        )
        email_field.send_keys("invalid-email")

        create_account_btn = driver.find_element(*CREATE_ACCOUNT_BUTTON)
        create_account_btn.click()

        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//*[contains(text(), 'Ошибка')]"))
        )

        error_element = driver.find_element(By.XPATH, "//*[contains(text(), 'Ошибка')]")
        assert error_element.is_displayed()
        assert "Ошибка" in error_element.text

    def test_registration_existing_user(self, driver):
        existing_email = "test@example.com"
        existing_password = "password123"

        login_btn = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(LOGIN_REG_BUTTON)
        )
        login_btn.click()

        no_account_btn = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(NO_ACCOUNT_BUTTON)
        )
        no_account_btn.click()

        email_field = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(REG_EMAIL_INPUT)
        )
        email_field.send_keys(existing_email)

        password_field = driver.find_element(*REG_PASSWORD_INPUT)
        password_field.send_keys(existing_password)

        confirm_password_field = driver.find_element(*REG_CONFIRM_PASSWORD_INPUT)
        confirm_password_field.send_keys(existing_password)

        create_account_btn = driver.find_element(*CREATE_ACCOUNT_BUTTON)
        create_account_btn.click()

        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//*[contains(text(), 'Ошибка')]"))
        )

        error_element = driver.find_element(By.XPATH, "//*[contains(text(), 'Ошибка')]")
        assert error_element.is_displayed()
        assert "Ошибка" in error_element.text