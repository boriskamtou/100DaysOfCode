from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_driver_path = 'C:\development\chromedriver'

driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get('https://www.python.org/')

all_dates = driver.find_elements(By.CSS_SELECTOR, ".event-widget time[datetime]")
all_event_names = driver.find_elements(By.CSS_SELECTOR, ".event-widget .menu a")

dates = []
names = []
my_dict = {}

for date in all_dates:
    dates.append(date)

for link in all_event_names:
    names.append(link)

my_dict = {}

for i in range(len(names)):
    my_dict.update(
        {
            i: {
                'date': dates[i].text,
                'name': names[i].text
            }
        }
    )

print(my_dict)

driver.quit()
