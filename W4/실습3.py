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

print(scores[0])
print(scores[1])
print(scores[2])