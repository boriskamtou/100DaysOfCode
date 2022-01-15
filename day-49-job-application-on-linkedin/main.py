from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.keys import Keys

chrome_driver_path = 'C:\development\chromedriver'

driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get(
    'https://www.linkedin.com/jobs/search/?f_LF=f_AL&geoId=102257491&keywords=python%20developer&location=London%2C%20England%2C%20United%20Kingdom&redirect=false&position=1&pageNum=0')

sign_in_button = driver.find_element(By.CLASS_NAME, 'nav__button-secondary')

sign_in_button.click()


email_input = driver.find_element(By.NAME, 'session_key')
password_input = driver.find_element(By.NAME, 'session_password')
sign_in_button_form = driver.find_element(By.CLASS_NAME, 'from__button--floating')

email_input.send_keys('your email address')
password_input.send_keys('your password')
sign_in_button_form.click()

