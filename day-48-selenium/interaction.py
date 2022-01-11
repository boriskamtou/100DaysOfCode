from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome_driver_path = 'C:\development\chromedriver'

driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get('http://secure-retreat-92358.herokuapp.com/')

first_name = driver.find_element(By.NAME, 'fName')
last_name = driver.find_element(By.NAME, 'lName')
email = driver.find_element(By.NAME, 'email')
submit_button = driver.find_element(By.CSS_SELECTOR, 'button')

first_name.send_keys('Kamtou')
last_name.send_keys('Boris')
email.send_keys('boris@yahoo.com')
submit_button.send_keys(Keys.ENTER)
