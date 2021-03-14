# 의용메카트로닉스공학과 20195277 하유민

print("의용메카트로닉스공학과 20195277 하유민")

print("Welcome!")
g=input("Guess the number: ") # input 으로 숫자를 입력 받음 
guess = int(g) # 입력 받은 숫자를 int 형태로 guess 라는 변수에 저장 
if guess == 5: # 입력 받은 숫자가 5  라면 아래의 코드를 실행 
    print("You win!")

else:
    if guess > 5:
        print("Too high")
        
    else:
        print("Too low")
print("Game over!")
