import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

#user email and password for FL
userEmail = 'testkeys'
userPassword = 'testpassword'

driver = webdriver.Chrome()
driver.get('https://www.fallenlondon.com/') #Opens Chrome and Directs to Fallenlondon

# Block to be used to enable FB linking
# loginButtonFB = driver.find_element(By.CLASS_NAME, 'fb-root')
# ActionChains(driver).move_to_element(loginButtonFB).click(loginButtonFB).perform

emailField = driver.find_element(By.ID, 'emailAddress')
passwordField = driver.find_element(By.ID, 'password')

emailField.send_keys(userEmail)
passwordField.send_keys(userPassword)

time.sleep(15)
driver.close() #close window