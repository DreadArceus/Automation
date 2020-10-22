#!/usr/bin/env python3

import time
import webbrowser
from selenium import webdriver
from bs4 import BeautifulSoup

driver = webdriver.Safari()
driver.get('https://erp.lnmiit.ac.in/ugadm/Dashboard.aspx')
soupI = BeautifulSoup()

while True:
    if driver.current_url != 'https://erp.lnmiit.ac.in/ugadm/Dashboard.aspx':
        login = driver.find_elements_by_class_name('form-control')
        login[0].send_keys('LNMLZVLC')
        login[1].send_keys('MPPYLBR7UA')

        button = driver.find_element_by_name('Button1')
        button.click()
        print('login successful')
    soupN = BeautifulSoup(driver.page_source, 'lxml')
    if soupI == BeautifulSoup():
        soupI = soupN
    if str(soupI).find('Second') != str(soupN).find('Second'):
        print('IT\'S CHANGED')
        webbrowser.open(driver.current_url)
        soupI = soupN
    time.sleep(30)
    driver.refresh()

driver.quit()