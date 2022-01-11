from selenium import webdriver
from selenium.webdriver.common.by import By
import time

chrome_driver_path = 'C:\development\chromedriver'

driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get('http://orteil.dashnet.org/experiments/cookie/')

cookie_button = driver.find_element(By.ID, 'cookie')

is_page_open = True

timeout = time.time() + 5
five_min = time.time() + 60 * 5  # 5minutes

while is_page_open:

    cookie_button.click()

    if time.time() > timeout:
        money_tex = driver.find_element(By.ID, 'money').text
        money = int(money_tex)

        affordables = driver.find_elements(By.CSS_SELECTOR, '#store div b')
        affordables_text = [affordable.text for affordable in affordables]
        affordables_list = [affordable_text.split(' ')[-1] for affordable_text in affordables_text]
        for affordable in affordables_list:
            if len(affordable) != 0:
                aff_number = int(affordable.replace(',', ''))
                if money >= aff_number:
                    for affordable_text in affordables_text:
                        if aff_number in affordables_list:
                            most_affordable = driver.find_element(By.ID, f'buy{affordable_text[0]}')
                            most_affordable.click()

    timeout = time.time() + 5
    if time.time() > five_min:
        cookie_per_s = driver.find_element(By.ID, 'cps').text
        print(cookie_per_s)

        break
