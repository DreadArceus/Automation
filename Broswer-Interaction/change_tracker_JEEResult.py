#Made to track the JEE Result website updating on 11th september 2020

import webbrowser
# Import requests (to download the page)
import requests

# Import Time (to add a delay)
import time

# Import BeautifulSoup (to parse what we download)
from bs4 import BeautifulSoup

# set the url,
url = "https://jeemain.nta.nic.in/webinfo/public/home.aspx"
# set the headers like we are a browser, (this part i dont understand)
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}# download the homepage
responseI = requests.get(url, headers=headers)
# parse the downloaded homepage and grab all text, then,
soupI = BeautifulSoup(responseI.text, "lxml")

while True:
    # do the download-parse routine again
    responseN = requests.get(url, headers=headers)
    soupN = BeautifulSoup(responseN.text, "lxml")
    #The following if statement checks if the first occurence of "Result" has changed its position from when the program started or not
    if(str(soupN).find("Result") == str(soupI).find("Result")):
        print(str(soupN).find("Result"))
        time.sleep(30) #Wait for x amount of time before going again
        continue
    else:
        print(str(soupN).find("Result"))
        print("Its here!")
        webbrowser.open(url) #opens the result page
        exit(0)