from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome_driver_path = "/Users/me/Documents/development/chromedriver"
service = Service(chrome_driver_path)
driver = webdriver.Chrome(service=service)

# driver.get("https://en.wikipedia.org/wiki/Main_Page")
# number_of_articles = driver.find_element(By.XPATH, '//*[@id="articlecount"]/a[1]')
# # print(number_of_articles.text)
#
# # number_of_articles.click()
#
# current_events = driver.find_element(By.LINK_TEXT, "Current events")
# # current_events.click()
#
# search = driver.find_element(By.NAME, "search")
# search.send_keys("Python")
# search.send_keys(Keys.ENTER)

driver.get("https://secure-retreat-92358.herokuapp.com/")
first_name = driver.find_element(By.NAME, "fName")
last_name = driver.find_element(By.NAME, "lName")
email = driver.find_element(By.NAME, "email")
signup_button = driver.find_element(By.CSS_SELECTOR, "form button")

first_name.send_keys("Diamond")
last_name.send_keys("Tusks")
email.send_keys("diamondtusks@gmail.com")
signup_button.click()

# driver.close()