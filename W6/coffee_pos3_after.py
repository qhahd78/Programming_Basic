# 의용메카트로닉스공학과 20195277 하유민
print("의용메카트로닉스공학과 20195277 하유민")

from transactions import * 
import promotion
import starbuzz
# menu 모듈 불러오기 
import menu

items = ["DONUT", "LATTE", "FILTER", "MUFFIN"]
prices = [1.50, 2.20, 1.80, 1.20]
running = True

while running: 
    # 모듈 이름까지 같이 써주기 
    # 인수로 items 전달
    opt = menu.menu_list(items)
    # menu.menu_list(items)
    # option = 1 
    # for choice in items: 
    #     print(str(option)+". "+ choice)
    #     option = option + 1 
    # print(str(option)+ ". Quit")
    choice = int(input("Choose an option: "))
    if choice == opt:
        running = False
    else: 
        credit_card = input("Crecit card number: ")
        price = promotion.discount(prices[choice - 1])
        if input("Starbuzz card? ") == "Y":
            price = starbuzz.discount(price)
        save_transaction(price, credit_card, items[choice -1])