# 의용메카트로닉스공학과 20195277 하유민

print("의용메카트로닉스공학과 20195277 하유민")

import urllib.request

page = urllib.request.urlopen("http://cs.sch.ac.kr/prices.py")

text = page.read().decode("utf8")

price = text[172:176] # 인덱스 172:176까지 price 에 저장

print(price)
