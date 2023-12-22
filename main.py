import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

#user email and password for FL
userEmail = 'flautofarmer+testcase0@gmail.com'
userPassword = 'c4$_SmcYwzPsuRH'

#VARIABLES
currentArea = 'Where I am'
currentActions = 'Spoons I have'

#INACTIVE/UNUSED VARIABLES
travelButton = 'Use me to access map' 
accessLadybonesDistrict = 'variable used to open ladybones district' 
accessMolochStreet = 'variable used for moloch st access later' 

driver = webdriver.Chrome()
driver.get('https://www.fallenlondon.com/') #Opens Chrome and Directs to Fallenlondon
driver.fullscreen_window()

#this block enters Username/Password and enters login
emailField = driver.find_element(By.ID, 'emailAddress')
passwordField = driver.find_element(By.ID, 'password')
loginButtonFL = driver.find_element(By.CSS_SELECTOR, 'button.button--primary')
emailField.send_keys(userEmail)
passwordField.send_keys(userPassword)
ActionChains(driver).click(loginButtonFL).perform()
time.sleep(3)


 #FUNCTIONS
def getCurrentArea():
    global currentArea 
    currentArea = driver.find_element(By.CSS_SELECTOR, 'p.welcome__current-area').text.replace(',', '')
    return 
def getCurrentActions():
    global currentActions 
    currentActions = driver.find_element(By.XPATH, '//*[@id="root"]/div/div[2]/div[4]/div[1]/div/div[1]/ul[1]/li[1]/div[2]/div/div/span/div[1]').text
    return

#INACTIVE/UNUSED FUNCTIONS
def getTravelButton(): 
    global travelButton
    travelButton = driver.find_element(By.XPATH, '//*[@id="root"]/div/div[2]/div[4]/div[1]/div/div[3]/div/div/button')
    return
def getLadybonesDistrict():
    global accessLadybonesDistrict
    accessLadybonesDistrict = driver.find_element(By.XPATH, '/html/body/div[11]/div/div/div[1]/div[1]/div[5]/div[2]/div/div/div')
    return
def getMolochStreet(): 
    global accessMolochStreet
    accessMolochStreet = driver.find_element(By.XPATH, '/html/body/div[11]/div/div/div[1]/div[1]/div[5]/div[15]/div/div/div')
    return
#xpath copy/pasted. POTENTIAL BREAKPOINT!!!

#PENDING VARIABLE APPLICATION
# if currentArea != 'Moloch Street':
#     getTravelButton()
#     ActionChains(driver).click(travelButton).perform()
#     time.sleep(2)
#     getLadybonesDistrict()
#     ActionChains(driver).click(accessLadybonesDistrict).perform
#     time.sleep(2)
#     getMolochStreet()
#     ActionChains(driver).click(accessMolochStreet).perform()

getCurrentActions()
getCurrentArea()

match currentArea:
    case 'Moloch Street':
        pass
    case 'Spite':
        pass
    case 'The University':
        pass
    case 'The Singing Mandrake':
        pass
    case 'The Blind Helmsman':
        pass

time.sleep(5)
driver.close() #close window