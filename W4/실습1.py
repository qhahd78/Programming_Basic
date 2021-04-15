# 의용메카트로닉스공학과 20195277 하유민
print("의용메카트로닉스공학과 20195277 하유민")
highest_score = 0 
result_f = open("results.txt")

for line in result_f: 
    (name,score) = line.split()
    if float(score) > highest_score: 
        highest_score = float(score)

result_f.close()
print("The highest score was: ")
print(highest_score)