import datetime
import pandas_datareader.data as web

from urllib.request import urlopen
from bs4 import BeautifulSoup

now = datetime.datetime.now()
nowDate = now.strftime('%Y-%m-%d')
nowTime = now.strftime('%H:%M:%S')

startDate = now - datetime.timedelta(days = 7)

print('Date: ', nowDate)
print('Time: ', nowTime, '\n')

asx200 = web.DataReader('^AXJO', 'yahoo', startDate, nowDate)
asx200 = asx200.reset_index()
asx200 = asx200.loc[::-1]

asx200_today = round(asx200.iloc[0, 6], 2)
asx200_yesterday = round(asx200.iloc[1, 6], 2)

asx200_diff = round(asx200_today - asx200_yesterday, 2)
asx200_diffper = abs((asx200_diff / asx200_yesterday) * 100)

if asx200_today > asx200_yesterday:
    sign = '▲'
elif asx200_today == asx200_yesterday:
    sign = ''
else:
    sign = '▼'

print("Current S&P/ASX 200 Close:", asx200_today,
      sign, asx200_diff, '(', sign, round(asx200_diffper, 2), '%', ')','\n')
print('<The Australian Financial Review - Equity markets>', '\n')

html = urlopen('https://www.afr.com/markets/equity-markets')
soup = BeautifulSoup(html.read(), 'html.parser')

titleList = soup.findAll('a', {'class':'_20-Rx'})
for title in titleList:
    print('*', title.get_text(), '\n')

print('Source: https://www.afr.com/markets/equity-markets')