from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_argument('--headless')
options.add_argument('--disable-gpu')  # Last I checked this was necessary.
PATH = "/home/emanuel/Documents/code_test/chromedriver"



#driver = webdriver.Chrome(PATH, options=options) #headless mode
driver = webdriver.Chrome(PATH,) #non headless mode
driver.implicitly_wait(10)

driver.get("https://www.keyhero.com/free-typing-test/")
print(driver.title)

search = driver.find_element_by_link_text("Log In / Sign Up").click()
logIn = driver.find_element_by_xpath( "//a[@href='/logincreate/']").click()

username = driver.find_element_by_id("id_usernamelogin")
username.send_keys("mansan2000")
password = driver.find_element_by_id("id_password")
password.send_keys("@Sanders6")
password.send_keys(Keys.RETURN)
#search.send_keys("iphone")
#search.send_keys(Keys.RETURN)


time.sleep(5)
#driver.quit()