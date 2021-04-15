# 의용메카트로닉스공학과 20195277 하유민
print("의용메카트로닉스공학과 20195277 하유민")

text = """
Soonchunhyang University
Department of Computer Science and Engineering
"""

# 파일 쓰기 
f = open("test.txt", "w")
f.write(text)
f.close()

# 파일 읽기 
f=open("test.txt")
lines = f.read()
print(lines.upper())