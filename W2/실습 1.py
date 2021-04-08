# 의용메카트로닉스공학과 20195277 하유민

print("의용메카트로닉스공학과 20195277 하유민")

import urllib.request # url 라이브러리안에 있는 request method 가져오기 

page = urllib.request.urlopen("http://cs.sch.ac.kr/prices.py") # page 변수에 url 을 저장 
text = page.read().decode("utf8") # text 변수에 utf8 로 문서를 해독하여 저장  

print(text) # text 변수를 출력한다.
