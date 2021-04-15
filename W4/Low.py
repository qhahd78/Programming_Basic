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

low_scores = []
low_scores.append(str(scores[-1]))
low_scores.append(str(scores[-2]))
low_scores.append(str(scores[-3]))

low_result = open("Low.txt", "w")

for i in low_scores:
    low_result.write(i)
    low_result.write("\n")
    
low_result.close()
