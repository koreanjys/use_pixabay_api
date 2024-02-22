import requests
import json
from urllib import parse
from dotenv import load_dotenv
import os
import sys
import urllib.request

# .env 불러오기
load_dotenv()
API_KEY = os.getenv("API_KEY")

# 검색할 이미지 파라미터 입력
q=input("검색어 입력: ")  # 검색어
maxImages=3 #이미지 숫자
image_type="all" #Accepted values: "all", "photo", "illustration", "vector"
path = "./images/"+q  #저장할 폴더
if not os.path.exists(path):
        os.makedirs(path)
else:
    print('폴더가 존재합니다')

url3 = f' https://pixabay.com/api/?key={API_KEY}&q={q}&image_type=photo&per_page={maxImages}'
res = requests.get(url3)
text= res.text
# print(text, type(text))

d = json.loads(text)

print(d, type(d))

# success=0
# for k in range(0,maxImages):
#     imgUrl=d['hits'][k]['webformatURL']
#     print("url:",imgUrl)
#     url = parse.urlparse(imgUrl) 
#     name, ext = os.path.splitext(url.path)
#     print(ext)


#     filename = f'{q}_{k+1}{ext}'      
#     saveUrl = path+'/'+filename #저장 경로 결정    
#     print(saveUrl)

#     #파일 저장   
#     req = urllib.request.Request(imgUrl, headers={'User-Agent': 'Mozilla/5.0'})
#     try:
#         imgUrl = urllib.request.urlopen(req).read() #웹 페이지 상의 이미지를 불러옴
#         with open(saveUrl,"wb") as f: #디렉토리 오픈
#             f.write(imgUrl) #파일 저장  
#         success+=1         

#     except urllib.error.HTTPError:
#         print('에러')
#         sys.exit(0)


# print('다운로드 성공 : '+str(success))