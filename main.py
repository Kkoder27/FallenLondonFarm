import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

#user email and password for FL
userEmail = 'flautofarmer+testcase0@gmail.com'
userPassword = 'c4$_SmcYwzPsuRH'

driver = webdriver.Chrome()
driver.get('https://www.fallenlondon.com/') #Opens Chrome and Directs to Fallenlondon


#this block enters Username/Password and enters login
emailField = driver.find_element(By.ID, 'emailAddress')
passwordField = driver.find_element(By.ID, 'password')
loginButtonFL = driver.find_element(By.CSS_SELECTOR, 'button.button--primary')
emailField.send_keys(userEmail)
passwordField.send_keys(userPassword)
ActionChains(driver).click(loginButtonFL).perform()



time.sleep(15)
driver.close() #close window