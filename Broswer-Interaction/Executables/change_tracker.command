#!/usr/bin/env python3

import webbrowser
# Import requests (to download the page)
import requests

# Import Time (to add a delay between the times the scape runs)
import time

# Import BeautifulSoup (to parse what we download)
from bs4 import BeautifulSoup

# set the url,
url = "https://jeemain.nta.nic.in/webinfo/public/home.aspx"
# set the headers like we are a browser,
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
# download the homepage
responseI = requests.get(url, headers=headers)
# parse the downloaded homepage and grab all text, then,
soupI = BeautifulSoup(responseI.text, "lxml")

while True:
    # download the homepage
    responseN = requests.get(url, headers=headers)
    # parse the downloaded homepage and grab all text, then,
    soupN = BeautifulSoup(responseN.text, "lxml")
    if(str(soupN).find("Result") == str(soupI).find("Result")):
        # wait,
        print(str(soupN).find("Result"))
        time.sleep(30)
        # continue with the script,
        continue
    else:
        print(str(soupN).find("Result"))
        print("Its here!")
        webbrowser.open(url)
        exit(0)