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

# scored 함수를 이용하여 정렬한다. default 가 오름차순이므로 reverse=True 를 설정하여 내림차순으로 정렬해준다. 
for each_score in sorted(scores.keys(), reverse= True):
    # if float(each_score) > 8.3 :  
    print('Surfer' + scores[each_score]+' scored ' + each_score)
