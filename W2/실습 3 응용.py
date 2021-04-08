# 의용메카트로닉스공학과 20195277 하유민

print("의용메카트로닉스공학과 20195277 하유민")

import urllib.request

page = urllib.request.urlopen("http://cs.sch.ac.kr/prices-loyalty.py")

text=page.read().decode("utf8")

where = text.find(">$")

start_of_price = where + 2

end_of_price = start_of_price +4

price = text[start_of_price:end_of_price]

# 여기부터는 응용 부분 
where2 = text.find("Price")
s = where2 + 9
e = s + 3
day = text[s : e]
print(day.upper())


print(price)

