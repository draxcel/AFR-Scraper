from urllib.request import urlopen
from bs4 import BeautifulSoup

import datetime
import pandas_datareader.data as web

now = datetime.datetime.now()
nowDate = now.strftime('%Y-%m-%d')
nowTime = now.strftime('%H:%M:%S')
yesDate = now - datetime.timedelta(1)

print('Date: ', nowDate)
print('Time: ', nowTime, '\n')

asx200 = web.DataReader('^AXJO', 'yahoo', yesDate, nowDate)
print("Current S&P/ASX 200 Close:", round(asx200.iloc[0, 5]), '\n')
print('<Financial Review Today>', '\n')

html = urlopen('https://www.afr.com/markets/equity-markets')
soup = BeautifulSoup(html.read(), 'html.parser')

titleList = soup.findAll('a', {'class':'_20-Rx'})
for title in titleList:
    print('●', title.get_text(), '\n')

print('Source: https://www.afr.com/markets/equity-markets')
