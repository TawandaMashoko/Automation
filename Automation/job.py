from selenium import webdriver
from selenium.webdriver.common.by import By
import time


def automate_data_entry():
    driver = webdriver.Chrome()
    driver.get('https://your-company-portal.com/login')

    # Login
    driver.find_element(By.ID, 'username').send_keys('your_username')
    driver.find_element(By.ID, 'password').send_keys('your_password')
    driver.find_element(By.ID, 'login-button').click()

    time.sleep(2)

    # Navigate to form
    driver.get('https://your-company-portal.com/form-entry')

    # Fill out form
    driver.find_element(By.ID, 'field1').send_keys('Data 1')
    driver.find_element(By.ID, 'field2').send_keys('Data 2')

    # Submit form
    driver.find_element(By.ID, 'submit').click()

    print("Form filled successfully!")

    driver.quit()


automate_data_entry()
