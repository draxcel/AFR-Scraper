# Financial Review Equity Market Scraper.
# Developer: Jun-hyeong Kim.
# Any inquiry: draxcel.blackfins@gmail.com

from urllib.request import urlopen
from bs4 import BeautifulSoup
from datetime import datetime

html = urlopen('https://www.afr.com/markets/equity-markets')
soup = BeautifulSoup(html.read(), 'html.parser')

now = datetime.now()
print('Date: {}/{}/{}'.format(now.year, now.month, now.day))
print('Time: {}:{}'.format(now.hour, now.minute), '\n')

titleList = soup.findAll('a', {'class':'_20-Rx'})
for title in titleList:
    print(title.get_text(), '\n')

print('☘ Good luck with your investment.')