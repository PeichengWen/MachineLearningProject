import urllib.request
import os
import time

import ssl 

ssl._create_default_https_context = ssl._create_unverified_context




try:
    url = 'https://finance.yahoo.com/quote/AAPL/key-statistics?p=AAPL'


    resp = urllib.request.urlopen(url)
    respData = resp.read()

    saveFile = open('withHeaders.html','w')
    saveFile.write(str(respData))
    saveFile.close()
except Exception as e:
    print(str(e))
