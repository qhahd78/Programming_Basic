# 의용메카트로닉스공학과 20195277 하유민
print("의용메카트로닉스공학과 20195277 하유민")

from transactions import * 
import menu

items = ["WORKOUT", "WEIGHTS", "BIKES"]
prices = [35.0, 10.0, 8.0]
running = True

while running: 
    opt = menu.menu_list(items)
    menu.menu_list(items)

    choice = int(input("Choose an option: "))
    if choice == opt:
        running = False
    else: 
        credit_card = input("Crecit card number: ")
        save_transaction(prices[choice-1], credit_card, items[choice -1])