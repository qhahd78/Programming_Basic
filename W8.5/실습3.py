# 의용메카트로닉스공학과 20195277 하유민 
print("의용메카트로닉스공학과 20195277 하유민")

try:
    x = float(input("숫자 입력: "))
    inverse = 1.0 / x 
except ValueError as e : 
    print(e)
except ZeroDivisionError as e:
    print("0으로 나눈 에러: " + str(e))
finally:
    print("예외가 발생하지 않거나 또는 발생할 수 있음.")