from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


def automate_gym_booking():
    driver = webdriver.Chrome()  # Use Chrome WebDriver
    driver.get('https://gym-website.com/login')  # URL of the gym website

    # Log in
    email = driver.find_element(By.ID, 'email')
    password = driver.find_element(By.ID, 'password')
    email.send_keys('your_email@example.com')
    password.send_keys('your_password')
    password.send_keys(Keys.RETURN)

    time.sleep(2)  # Wait for the login process to complete

    # Navigate to class booking page
    driver.get('https://gym-website.com/book-class')

    # Find and select the class you want to book
    class_button = driver.find_element(By.XPATH, '//button[text()="Book Class"]')
    class_button.click()

    # Confirm the booking
    confirm_button = driver.find_element(By.XPATH, '//button[text()="Confirm"]')
    confirm_button.click()

    print("Gym class successfully booked!")

    driver.quit()


automate_gym_booking()
