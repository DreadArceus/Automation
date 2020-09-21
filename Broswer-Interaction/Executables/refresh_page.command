#!/usr/bin/env python
import webbrowser
import time

webbrowser.open('https://jeemain.nta.nic.in/webinfo/public/home.aspx')
y = time.time()

while(1):
    x = time.time()
    if(x - y >= 5):
        webbrowser.open('https://jeemain.nta.nic.in/webinfo/public/home.aspx')
        y = x
