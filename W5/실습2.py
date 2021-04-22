# 빈 딕셔너리 생성 
scores = {}

# results.txt 를 열어준다. 
result_f = open("results.txt")

# result_f 한 줄당 아래의 코드를 적용한다. 
for line in result_f:
    # 공백을 기준으로 name 과 score로 나누어준 후 
    (name, score) = line.split()
    # scores 딕셔너리 안에 key 값을 score로, value 값을 name 으로 저장한다. 
    scores[score] = name

# result_f 를 닫는다. 
result_f.close()

print("The top scores were: ")

# scores key 개수 번 딕셔너리를 돌며 아래의 함수를 실행한다. 
for each_score in scores.keys():
    # scores[each_score] 는 each_score의 value 값으로 이름이 출력된다. 
    # each_score는 키값으로 점수가 출력된다.  
    print('Surfer' +scores[each_score]+ ' scored '+ each_score)