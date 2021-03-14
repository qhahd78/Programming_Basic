# 의용메카트로닉스공학과 20195277 하유민 

print("의용메카트로닉스공학과 20195277 하유민 ")
print("Welcome!")

guess = 0 # guess 값 초기화

while guess != 5: # guess 가 5가 아니면 아래의 코드 실행 
    g=input("Guess the number: ") # 값을 입력 받아 g 에 저장
    
    guess = int(g) # g 를 int 형으로 변환 후 guess 에 저장
    
    if guess == 5: # guess 가 5면 You win! 출력  
        print("You win!")
        
    else: # 5가 아닐 때 아래의 함수를 실행
        if guess > 5: # 5보다 크다면 Too high 출력 
            print("Too high")
        else: # 5보다 작다면 Too low 출력 
            print("Too low")
            
# 정답을 맞췄다면 while 문을 나와 Game over 출력
print("Game over!")
