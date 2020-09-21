#made for JEE Mains 2020 result on 11th september 2020
import webbrowser
import time

webbrowser.open('https://jeemain.nta.nic.in/webinfo/public/home.aspx') #opens URL in default browser
y = time.time()

while(1):
    x = time.time()
    if(x - y >= 5):
        webbrowser.open('https://jeemain.nta.nic.in/webinfo/public/home.aspx')
        y = x