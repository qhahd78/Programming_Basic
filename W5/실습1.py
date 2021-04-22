# 빈 리스트 2개를 생성 
scores = []
names = []

# results.txt 를 열어준다. 
result_f=open("results.txt")

# 열어준 txt 파일 한 줄당 아래의 코드를 실행한다. 
for line in result_f: 

    # 공백을 기준으로 name 과 score로 나누어준다. 
    (name,score) = line.split()
    # scores 리스트에 score 값을 float 형태로 append 
    scores.append(float(score))
    # names 리스트에 name 값을 append 
    names.append(name)

# result_f 파일을 닫는다. 
result_f.close()

# scores 리스트를 정렬한다. 
scores.sort()
scores.reverse()

# names 리스트를 정렬한다. 
names.sort()
names.reverse()

print("The highest scores were:")

print(names[0]+' with '+str(scores[0]))
print(names[1]+' with '+str(scores[1]))
print(names[2]+' with '+str(scores[2]))