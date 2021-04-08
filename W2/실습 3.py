# 의용메카트로닉스공학과 20195277 하유민

print("의용메카트로닉스공학과 20195277 하유민")

import urllib.request

page = urllib.request.urlopen("http://cs.sch.ac.kr/prices-loyalty.py")

text=page.read().decode("utf8")

where = text.find(">$") # >$ 이 발견된 첫 번째 인덱스 값을 반환한다. 

start_of_price = where + 2 # 가격이 시작되는 인덱스를 start_of_price 변수에 저장. 

end_of_price = start_of_price + 4 # 가격이 끝나는 인덱스를 end_of_price 변수에 저장

price = text[start_of_price:end_of_price] # 가격을 price 변수에 저장 

print(price)
