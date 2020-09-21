from selenium import webdriver 
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC 
from selenium.webdriver.common.keys import Keys 
from selenium.webdriver.common.by import By 
import time

driver = webdriver.Safari()

driver.get("https://web.whatsapp.com/")
wait = WebDriverWait(driver, 100)

target = ['"Lalit Lakshay"', '"Tamish New"', '"Aaryuman"']

string = "The result is out, go check."

for i in range(3):
    x_arg = '//span[contains(@title,' + target[i] + ')]'
    group_title = wait.until(EC.presence_of_element_located((
    By.XPATH, x_arg)))
    print (group_title)
    print ("Wait for few seconds")
    group_title.click()
    message = driver.find_elements_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')[0]
    message.send_keys(string)
    sendbutton = driver.find_elements_by_xpath('//*[@id="main"]/footer/div[1]/div[3]/button')[0]
    sendbutton.click()
time.sleep(2) #waiting for whatsapp to process the messages
driver.close()