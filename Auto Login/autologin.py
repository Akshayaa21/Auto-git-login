from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By # "By" class is used to extract elements form the web pages by using class name ID or CSS selector

#dummy login details
username = "shaya211"
password = "rH@nDk7pREg9KgK"

url= "https://www.github.com/login"

chrome_options = Options() #Options() is used for customizing the behaviour of Chrome Browser with selenium
chrome_options.add_experimental_option("detach", True)
# The above line is to keep the web brower open since its default is to close automatically once the process has executed, It is done by setting the detach parameter to True .
driver = webdriver.Chrome(options=chrome_options)

driver.implicitly_wait(3)# Waiting for 3 seconds after creating the object and opening the URL

driver.get(url)

driver.find_element(By.CSS_SELECTOR,'input[name="login"]').send_keys(username)# This line finds the element on the web page that has CSS_SELECTOR "input-name=login" and sends the value  back to the username variable
driver.find_element(By.CSS_SELECTOR, 'input[name="password"]').send_keys(password)
driver.find_element(By.CSS_SELECTOR, 'input[type="submit"]').click()# This line finds the "input[type=submit]" in the web page and then clicks on that element resulting in the submission of the account

print("logged in !")

driver.get('https://www.github.com/shaya211')



