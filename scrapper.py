import os 
import time 
from selenium import webdriver
import selenium.webdriver.chrome.service as service

service = service.Service(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'chromedriver'))
service.start()
capabilities = {'chrome.binary': '/usr/bin/google-chrome'}
driver = webdriver.Remote(service.service_url, capabilities)
driver.get('http://canvas.cmu.edu');

username_field = driver.find_element_by_id("j_username")
password_field = driver.find_element_by_id("j_password")
login_button = driver.find_element_by_class_name("loginbutton")

username_field.send_keys("")
password_field.send_keys("")
login_button.click()
# gives enough time for Duo to load the iframe, increase time if it bugs
time.sleep(5)

driver.switch_to.frame(driver.find_element_by_id("duo_iframe"))
duo_auth_button = driver.find_element_by_css_selector("button.positive.auth-button")
duo_auth_button.click()
# gives you enough time to authenticate on your phone
time.sleep(10) 
driver.switch_to.default_content()
# code to scrap the scores of students 
time.sleep(1000) # Let the user actually see something!
driver.quit()
