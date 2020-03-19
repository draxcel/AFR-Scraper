# 호주 파이낸션 리뷰 주식시장 기사 스크래퍼
# 파파고 API를 이용한 자동 번역 버전.
# 개발자: 김준형.
# 기타 문의: draxcel.blackfins@gmail.com

from urllib.request import urlopen
from bs4 import BeautifulSoup
from datetime import datetime
import requests

now = datetime.now()
print('Date: {}/{}/{}'.format(now.year, now.month, now.day))
print('Time: {}:{}'.format(now.hour, now.minute), '\n')

html = urlopen('https://www.afr.com/markets/equity-markets')
soup = BeautifulSoup(html.read(), 'html.parser')

text = []

titleList = soup.findAll('a', {'class':'_20-Rx'})
for title in titleList:
    text.append(title.get_text())

text = '\n'.join(text)

papago_url = 'https://openapi.naver.com/v1/papago/n2mt'
headers = {'X-Naver-Client-Id': 'API 클라이언트 ID 입력', 'X-Naver-Client-Secret': 'API 클라이언트 PW 입력'}
params = {'source': 'en', 'target': 'ko', 'text': text}
response = requests.post(papago_url, headers = headers, data = params)
 
result = response.json() 
print(result, '\n')

print('☘ 좋은 결과 있으시길 바랍니다.')