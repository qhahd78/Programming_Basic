# 의용메카트로닉스공학과 20195277 하유민
print("의용메카트로닉스공학과 20195277 하유민")

from transactions import * 
# 할인 가격을 계산하는 promotion 함수 불러오기 
from promotion import *

items = ["DONUT", "LATTE", "FILTER", "MUFFIN"]
prices = [1.50, 2.20, 1.80, 1.20]
running = True

# running = True 이므로 아래의 코드는 무조건 실행된다. 
while running:
    # option = 1 로 정의 
    option = 1 
    # items 에 있는 원소가 choice로 들어가고, choice 의 개수만큼 
    #  아래의 코드가 반복된다. 
    for choice in items : 
        # 1. items[choice] 를 출력한다. 
        # option 이 한 바퀴 돌 때마다 1씩 추가 되므로 1,2,3,4으로 늘어난다. 
        print(str(option) + ". "+ choice)
        # 한 원소를 프린트 하고 option 에 1을 더해준다. 
        option = option + 1
    # for 문이 끝나고, option은 5가 들어가 있다. 5. QUit 프린트. 
    print(str(option)+ ". Quit")
    # option 값을 int 형태로 입력 받아 choice 에 넣어준다.  
    choice = int(input("Choose an option: "))

    # 만약 choice 가 option 값과 같다면, 
    if choice == option:
        # while 문은 한 번만 돈다. (choice를 올바르게 했으면. )
        running = False
    else: 
        credit_card = input("Crecit card number: ")
        # new_price 를 정의한다. discount 함수에 인수로 prices[choice-1] 를 전달.
        new_price = discount(prices[choice-1])
        save_transaction(new_price, credit_card, items[choice -1])