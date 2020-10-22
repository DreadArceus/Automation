from selenium import webdriver 
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC 
from selenium.webdriver.common.keys import Keys 
from selenium.webdriver.common.by import By 
import time

driver = webdriver.Safari() #Assigning the desired browser's web driver

driver.get("https://web.whatsapp.com/") #Website to operate on
wait = WebDriverWait(driver, 60) #Needed to allow WhatsApp's QR code scan

target = '"Umesh"' #Recipient name to find in whatsapp

string = "Testing whatsapp via python..." #Actual Message

#The following block of code finds the target, clicks on it, finds the message box, clicks on it,
# sends keystrokes corresponding to the string and then clicks the send button.
x_arg = '//span[contains(@title,' + target + ')]'
group_title = wait.until(EC.presence_of_element_located((
By.XPATH, x_arg)))
print (group_title)
print ("Wait for few seconds") #To account for delays by whatsapp (removable)
group_title.click()
message = driver.find_elements_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')[0]
message.send_keys(string)
sendbutton = driver.find_elements_by_xpath('//*[@id="main"]/footer/div[1]/div[3]/button')[0]
sendbutton.click()
for i in range(100):
    message.send_keys(f'{i}')
    message.send_keys(Keys.RETURN)
time.sleep(6)
driver.close()