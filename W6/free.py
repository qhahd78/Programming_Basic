# 의용메카트로닉스공학과 20195277 하유민 
print("의용메카트로닉스공학과 20195277 하유민 ")

# 수강신청 신청 확인 취소 프로그램 

subjects =['교양1', '전공1', '전공2', '전공3', '교양2']
choice = ['삭제', '수정', '추가']
option =1 
running = True

while running : 
    for subject in subjects : 
        print(str(option)+". "+ subject)
        option = option + 1 
    print(str(option)+". "+"끝내기")

    subject = input(" 수정할 과목을 선택해주세요. ")
    if subject == option : 
        running = False 

    else : 
        option = 1
        for choose in choice : 
            print(str(option)+". "+choose)
            option = option + 1 
        print(str(option)+". "+"끝내기")
    