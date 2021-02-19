from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
PATH = "/home/emanuel/Documents/code_test/chromedriver"

driver = webdriver.Chrome(PATH)

driver.get("https://www.ebay.com/")
print(driver.title)

search = driver.find_element_by_name("_nkw")
search.send_keys("iphone")
search.send_keys(Keys.RETURN)
time.sleep(5)
driver.quit()