from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import pytest



def test_on_board():
    #options = Options.add_experimental_option('excludeSwitches', ['enable-logging'])
    #chrome_driver = webdriver.Chrome('./chromedriver', options=options)
    chrome_driver = webdriver.Chrome()

    chrome_driver.get('https://onboard.henrymeds.com/')
    
    page_title = "Phentermine Appointment - Henry Meds"
    assert page_title == chrome_driver.title

    chrome_driver.find_element(By.XPATH, "//button[10]" ).click()
    selected_url = "https://onboard.henrymeds.com/?state=delta"
    assert selected_url == chrome_driver.current_url

    chrome_driver.close()
