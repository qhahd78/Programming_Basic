# 의용메카트로닉스공학과 20195277 하유민
print("의용메카트로닉스공학과 20195277 하유민")

scores = []
result_f = open("results.txt")

for line in result_f: 
    (name, score) = line.split()
    scores.append(float(score))

result_f.close()

scores.sort()
scores.reverse()

print(scores)

# 새로운 배열 low_scores 생성
low_scores = []

# append 로 낮은 점수 3개를 배열에 넣어준다. 
low_scores.append(str(scores[-1]))
low_scores.append(str(scores[-2]))
low_scores.append(str(scores[-3]))

# Low.txt 를 열어준다. (write)
low_result = open("Low.txt", "w")

# low_scores 를 한 바퀴 돌면서 한 줄에 하나씩 배열의 요소 하나를 출력해준다. 
for i in low_scores:
    # 배열의 요소 하나를 출력
    low_result.write(i)
    # 한 줄씩 출력하기 위해 줄 바꿈 
    low_result.write("\n")

# 파일 닫기 
low_result.close()
