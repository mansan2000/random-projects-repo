from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
import time
from selenium.webdriver.chrome.options import Options

import pyimgur

import os
from twilio.rest import Client

#logic for headless mode
options = Options()
options.add_argument('--headless')
options.add_argument('--disable-gpu')  
PATH = "/home/emanuel/Documents/code_test/chromedriver"



#driver = webdriver.Chrome(PATH, options=options) #headless mode
driver = webdriver.Chrome(PATH,) #non headless mode
driver.implicitly_wait(10)

#open page 
driver.get("https://padlock.idm.uab.edu/cas/login?service=https%3A%2F%2Fhealthcheck.staysafetogether.org%2F14")

#fill in username and password
username = driver.find_element_by_id("username")
username.send_keys("emanuels") #username
password = driver.find_element_by_id("password")
password.send_keys("@1220Josephemanuel") #password
password.send_keys(Keys.RETURN)

#check to see if the form has already been filled out. if it hasn't run through code, if it has skip to except
try:
        driver.find_element_by_id("wfPageNextId1").click()
        time.sleep(2)
        driver.find_element_by_class_name("input-checkbox-faux").click()
        time.sleep(2)
        driver.find_element_by_id("wfPageNextId2").click()
        time.sleep(2)
        driver.find_element_by_xpath("//label[@id='tfa_41-L'] //span[@class='input-radio-faux']").click()
        driver.find_element_by_id("wfPageNextId3").click()
        driver.find_element_by_xpath("//label[@id='tfa_75-L'] //span[@class='input-radio-faux']").click() #this line can be commented out if you want to test the script but not select the last box and actually run it 
        driver.find_element_by_xpath("//div[@id='15-A'] //input[@class='primaryAction']").click() #this line can be commented out if you want to fill out the entire healthcheck but not submit it 
        time.sleep(2)
except NoSuchElementException:
        driver.find_element_by_id("ppt_button").click()
        time.sleep(2)
        driver.save_screenshot("screenshot.png")


#upload screenshot to imgur so that I can access it with a url
CLIENT_ID = "2c17993a469b06f"
PATH = "screenshot.png"

im = pyimgur.Imgur(CLIENT_ID)
uploaded_image = im.upload_image(PATH, title="Uploaded with PyImgur")

#twilio code for sending the image to my phone
account_sid = 'AC14f5e19d497b00912b95afbdcbc1a697'
auth_token = '8427bab06299a562e98910883e93b96e'
client = Client(account_sid, auth_token)

message = client.messages \
                .create(
                     body="Healthcheck!",  
                     from_='+16094736880',
                     media_url=[uploaded_image.link],
                     to='+13347074842'                                      #phone number to send the screenshot to 
                 )

print(message.sid)

time.sleep(5)
driver.quit()