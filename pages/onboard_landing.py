from selenium.webdriver.common.by import By
import time

class OnboardLanding:
    def __init__(self, driver):
        self.driver = driver
        self.utah_button_locator = (By.XPATH, "//button[10]")
        self.second_time_slot_button = (By.XPATH, "//button[2]")
        self.provider_continue_button = (By.CSS_SELECTOR, ".MuiButtonBase-root")
        self.first_name_field = (By.ID, ":r0:")
        self.last_name_field = (By.ID, ":r1")
        self.email_field = (By.ID, ":r2:")
        self.date_of_birth = (By.ID, ":r3:")
        self.phone_number = (By.ID, ":r4:")
        self.sex_dropdown = (By.XPATH, "//div[@id='root']/div/div/div/div[2]/form/div/div[6]/div/div/select")
        self.pronouns_dropdown = (By.XPATH, "//div[@id='root']/div/div/div/div[2]/form/div/div[7]/div/div/select")
        self.details_continue_button = (By.ID, ":r5:")
        self.address1 = (By.ID, ":r6:")
        self.address2 = (By.ID, ":r7:")
        self.city = (By.ID, ":r8:")
        self.zipcode = (By.ID, ":rb:")
        self.contune_to_billing = (By.ID, ":rc:")



    
    def click_utah_button(self):
        self.driver.find_element(*self.utah_button_locator).click()
        time.sleep(1)

    def click_time_slot_button(self):
        self.driver.find_element(*self.second_time_slot_button).click()
        time.sleep(1)
    
    def click_provider_continue_button(self):
        self.driver.find_element(*self.provider_continue_button).click()
        time.sleep(1)

    def enter_first_name(self, first_name):
        self.driver.find_element(*self.first_name_field).send_keys(first_name)

    def enter_last_name(self, last_name):
        self.driver.find_element(*self.first_name_field).send_keys(last_name)
    
    def enter_email(self, email):
        self.driver.find_element(*self.email_field).send_keys(email)

    def enter_dob(self, dob):
        self.driver.find_element(*self.date_of_birth).send_keys(dob)

    def enter_phone_number(self, phone):
        self.driver.find_element(*self.phone_number).send_keys(phone)
    
    def select_sex(self):
        self.driver.find_element(*self.sex_dropdown).click()
        dropdown = self.driver.find_element(*self.sex_dropdown)
        dropdown.find_element(By.XPATH,"//option[. = 'Male']" ).click()

    def select_pronouns(self):
        self.driver.find_element(*self.pronouns_dropdown).click()
        dropdown = self.driver.find_element(*self.pronouns_dropdown)
        dropdown.find_element(By.XPATH, "//option[. = 'He/Him']").click()
    
    def click_details_continue(self):
        self.driver.find_element(*self.details_continue_button).click()
        time.sleep(1)

    def enter_address1(self, address):
        self.driver.find_elements(*self.address1).sendkeys(address)

    def enter_city(self, city):
        self.driver.find_elements(*self.city).sendkeys(city)
    
    def ender_zip(self, zipcode):
        self.driver.find_elements(*self.zipcode).sendkeys(zipcode)

    def click_continue_to_billing(self):
        self.driver.find_elements(*self.contune_to_billing).click()
        time.sleep(1)

