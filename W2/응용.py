# 의용메카트로닉스공학과 20195277 하유민

print("의용메카트로닉스공학과 20195277 하유민")


# 약수 출력 프로그램

print("약수 출력 프로그램입니다. ")
fnum = input("숫자를 입력해보세요. ")

n = 0 # 1씩 증가 하는 수 
num = int(fnum) # 약수를 구하고 싶은 수
i = 0 # 약수의 개수를 세주는 수 


while n <= num : # n 가 num 보다 작거나 같을 때까지 while 문을 반복한다. 
    n = n +1 # 한 바퀴 돌 때마다 n 증가 
    if num % n !=  0 :  # 만약 num 나누기 n 의 나머지가 있을 경우 
        continue # 통과 한다. 
    else: # 만약 num 나누기 n 의 나머지가 없을 경우 (약수에 해당한다. )
        i= i+1 # 약수의 개수 세는 i 를 1씩 증가 시킨다. 
        print(n) # 약수를 출력한다. 

print("약수 구하기 끝 ") # while 문이 끝나면 다음 문장을 출력한다.
print("약수는 총", i ,"개 입니다.") # 약수의 총 개수를 출력한다. 
    



