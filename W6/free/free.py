# 의용메카트로닉스공학과 20195277 하유민 
print("의용메카트로닉스공학과 20195277 하유민 ")

# 1. 원하는 계산기 기능 고르기 (덧셈 뺄셈 곱셈 제곱 나눗셈 )
# 2. 두 개의 숫자를 입력 받아 연산 실행 
# 3. 결과 값을 출력해준다. 

# 모듈 호출
import plus
import minus
import multiple
import divide

# 기본 값 세팅
carcul = ['덧셈', '뺄셈', '곱셈','나눗셈']
repeat = True
result = 0

# while 문으로 아래의 코드를 무한 반복 
while repeat : 
    i = 1
    # carcul 리스트를 한 번 돌면서 보기를 출력 
    for choice in carcul:
        print(str(i)+ "." +choice)
        i = i+1
    print(str(i)+". Quit")
    # 기능의 번호를 입력 받는다. 
    choice = int(input("원하는 계산기의 기능을 골라주세요. "))

    # 5일 경우 바로 프로그램 종료 
    if choice == 5 : 
        break
    
    # 5보다 작은 경우 (보기에 있는 번호를 골랐을 경우)
    if choice <= 5 :
        # repeat 을 False 로 변경
        repeat = False
        # 연산할 숫자 2개를 입력 받는다. 
        num1 = int(input("첫 번째 숫자를 입력하세요. "))
        num2 = int(input("두 번째 숫자를 입력하세요. "))
        
        # 1일 경우 덧셈 모듈 실행 
        if choice == 1 : 
            result = plus.Plus(num1, num2)
            print(result)
        
        # 2일 경우 뺄셈 모듈 실행 
        elif choice == 2 : 
            result = minus.Minus(num1,num2)
            print(result)

        # 3일 경우 곱셈 모듈 실행 
        elif choice == 3 : 
            result = multiple.Multiple(num1,num2)
            print(result)

        # 4일 경우 나누기 모듈 실행 
        elif choice == 4 : 
            result = divide.Divide(num1,num2)
            print(result)
            
    