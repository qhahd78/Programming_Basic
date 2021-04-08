# 의용메카트로닉스공학과 20195277 하유민

print("의용메카트로닉스공학과 20195277 하유민")

import urllib.request

price = 9

# 가격이 4를 넘을 때만 아래의 코드가 출력되게 함 
while price > 4:
    page = urllib.request.urlopen("http://cs.sch.ac.kr/prices-loyalty.py")
    text = page.read().decode("utf8")
    where = text.find(">$")
    start_of_price = where +2
    end_of_price = start_of_price + 4
    
    # 가격 부분 슬라이싱 
    price = float(text[start_of_price:end_of_price])
    
    # 시간 부분 슬라이싱 
    time = text.find("Price")
    t = time + 9
    e = t + 20
    ff = text[t:e]
    
    print("가격이 4달러를 넘었습니다 ! 가격, 날짜, 시간을 출력합니다. ")
    print(price)
    
    # 시간 출력 
    print(ff)
    
# 원하는 가격의 범위가 아니라면 while 문을 빠져나오고 다음을 출력한다.
print("원하는 가격이 아닙니다.")

