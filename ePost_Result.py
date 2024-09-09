import requests
from bs4 import BeautifulSoup

# URL 설정
url = "https://service.epost.go.kr/trace.RetrieveDomRigiTraceList.comm?sid1=1102326109990&displayHeader="

# 웹 페이지 가져오기
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# 테이블 찾기
table = soup.find('table', {'id': 'processTable'})



# 마지막 행 찾기
last_row = table.find_all('tr')[-1]
columns = last_row.find_all('td')

# 각 열의 값을 변수에 담기
column_values = [col.text.strip() for col in columns]

# 변수에 담기
var1, var2, var3, var4 = column_values  # 필요한 변수 개수에 맞게 조정

#print(f"Var1: {var1}, Var2: {var2}, Var3: {var3}, Var4: {var4}")
msg = var4.replace('\n','').replace(' ','').replace('\t','')

print(msg)

#u8QPHpkZe9C7B9v%2Fgjvh3VQNgqs%2BgvHCKdy7v4Oa0wWMtXL10EMG9Y634m0FckWe13ts7riEn5qJpD%2FXLQeyRg%3D%3D
#u8QPHpkZe9C7B9v/gjvh3VQNgqs+gvHCKdy7v4Oa0wWMtXL10EMG9Y634m0FckWe13ts7riEn5qJpD/XLQeyRg==

import requests

url = 'http://openapi.epost.go.kr/trace/retrieveLongitudinalCombinedService/retrieveLongitudinalCombinedService/getLongitudinalCombinedList'
params ={'serviceKey' : 'u8QPHpkZe9C7B9v%2Fgjvh3VQNgqs%2BgvHCKdy7v4Oa0wWMtXL10EMG9Y634m0FckWe13ts7riEn5qJpD%2FXLQeyRg%3D%3D', 'rgist' : '1102326109990' }

response = requests.get(url, params=params)
print(response.content)