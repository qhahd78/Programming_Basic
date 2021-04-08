# 의용메카트로닉스공학과 20195277 하유민

print("의용메카트로닉스공학과 20195277 하유민")

import urllib.request

price = 99.99
while price > 4.74:
    page = urllib.request.urlopen("http://cs.sch.ac.kr/prices-loyalty.py")
    text = page.read().decode("utf8")
    where = text.find(">$")
    start_of_price = where +2
    end_of_price = start_of_price + 4
    price = float(text[start_of_price:end_of_price])

    # 여기부터 응용부분 
    time = text.find("Mar")
    s = time + 7
    e = s + 13
    t = text[s:e]

print(price)
print(t)
