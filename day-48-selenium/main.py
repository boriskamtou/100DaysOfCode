from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_driver_path = 'C:\development\chromedriver'

driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get(
    'https://www.amazon.com/AmazonBasics-Nylon-Braided-Lightning-Cable/dp/B082T6GVKJ/ref=sr_1_14?keywords=amazonbasics&pd_rd_r=06107e94-b0ab-4df2-a614-4bf3f256c94f&pd_rd_w=iTmmp&pd_rd_wg=4V8Am&pf_rd_p=9349ffb9-3aaa-476f-8532-6a4a5c3da3e7&pf_rd_r=2NG7S8YHCF4VPRF90120&qid=1641685227&sr=8-14&th=1')

price = driver.find_element('//*[@id="corePrice_desktop"]/div/table/tbody/tr/td[2]/span[1]/span[2]')
print(price.text)

driver.quit()
