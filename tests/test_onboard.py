import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from pages.onboard_landing import OnboardLanding
import time

def test_correct_landing():
    driver = webdriver.Chrome()
    landing_page = OnboardLanding(driver)
    driver.get('https://onboard.henrymeds.com/')
    page_title = "Phentermine Appointment - Henry Meds"
    assert page_title == driver.title
    driver.quit()

def test_successful_click_to_schedule_page():
    driver = webdriver.Chrome()
    landing_page = OnboardLanding(driver)
    driver.get('https://onboard.henrymeds.com/')
    time.sleep(1)
    landing_page.click_utah_button()
    assert driver.current_url == "https://onboard.henrymeds.com/?state=utah"
    driver.quit()

def test_happypath():
    driver = webdriver.Chrome()
    landing_page = OnboardLanding(driver)
    driver.get('https://onboard.henrymeds.com/')
    time.sleep(1)
    landing_page.click_utah_button()
    landing_page.click_time_slot_button()
    assert landing_page.provider_continue_button

    landing_page.click_provider_continue_button()
    landing_page.enter_first_name("foo")
    landing_page.enter_last_name("bar")
    landing_page.enter_email("foobar@mail.com")
    landing_page.enter_dob("12/25/1975")
    landing_page.enter_phone_number("(555) 255-7310")
    landing_page.select_sex()
    landing_page.select_pronouns()
    landing_page.click_details_continue()
    landing_page.enter_address1("123 my street")
    landing_page.enter_city("Sandy")
    landing_page.ender_zip("84043")
    landing_page.click_continue_to_billing

    driver.quit()
