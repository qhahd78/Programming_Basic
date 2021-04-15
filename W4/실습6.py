# 의용메카트로닉스공학과 20195277 하유민
print("의용메카트로닉스공학과 20195277 하유민")

for i in range(5) : 
    print(i)

print(list(range(5)))

result_f = open("results.txt")
for line in result_f: 
    print(line)

print(list(result_f))
result_f.close()
result_f = open("results.txt")
print(list(result_f))
result_f.seek(0)
text = result_f.read()
print(text)
text.split()
s= "Computer"
print(list(s))