print("의용메카트로닉스공학과 20195277 하유민")

import urllib.request

def get_price():
    page = urllib.request.urlopen("http://cs.sch.ac.kr/prices-loyalty.py")
    text = page.read().decode("utf8")
    where = text.find(">$")
    start_of_price = where + 2
    end_of_price = start_of_price +4
    return text [start_of_price:end_of_price]

price = get_price()
print(price)
