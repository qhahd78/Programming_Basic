scores = {}
result_f = open("results.txt")

for line in result_f : 
    (name, score) = line.split()
    scores[score] = name

result_f.close()

print("The top scores were: ")
for each_score in sorted(scores.keys(), reverse= True):
    if float(each_score) > 8.3 :  
        print('Surfer' + scores[each_score]+'scored' + each_score)
