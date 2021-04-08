import urllib.request
import time

print("의용메카트로닉스공학과 20195277 하유민")

def get_price():
    page = urllib.request.urlopen("http://cs.sch.ac.kr/prices-loyalty.py")
    text = page.read().decode("utf8")
    where = text.find(">$")
    start_of_price = where + 2
    end_of_price = start_of_price + 4
    return float(text[start_of_price:end_of_price])

price_now = input("Do you want to see the price now (Y/N)")
if price_now == "Y":
    print(get_price())
else:
    price = 99.99
    while price > 4.74:
        time.sleep(3)
        price = get_price()
    print("Buy!")
