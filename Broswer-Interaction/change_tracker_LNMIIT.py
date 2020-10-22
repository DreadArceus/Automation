import webbrowser
import requests
import time
from bs4 import BeautifulSoup

url = "https://admissions.lnmiit.ac.in/ugadmissions/JEE-Main-Mode.html"
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
responseI = requests.get(url, headers = headers)
soupI = BeautifulSoup(responseI.text, "lxml")
i = 1
while True:
    responseN = requests.get(url, headers = headers)
    soupN = BeautifulSoup(responseN.text, "lxml")
    if(soupI.get_text() == soupN.get_text()):
        print("Not yet..." + str(i))
        i += 1
        time.sleep(30)
        continue
    else:
        print("It's changed!")
        webbrowser.open(url)
        exit(0)