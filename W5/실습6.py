# 리스트의 메서드를 사용하여 단어의 개수를 리턴하는 함수 
def wCount(word):
    wlist = []
    # text 변수의 내용을 공백 문자를 기준으로 분리하여 리스트를 생성 
    for wd in text.split():
        wlist.append(wd)
    
    # 생성된 리스트의 개수를 세어 리턴한다. 
    cnt = wlist.count(word)
    return cnt

f = open("Imagine.txt")
text = f.read()

w = "Imagine"
n = wCount(w) # 함수 호출
print(w + ":" + str(n)) # 단어 개수 출력 

wlist = ["Imagine", "people", "dreamer"]
s = {}

for wd in wlist : 
    n = wCount(wd)
    s[wd] = n

print(s)