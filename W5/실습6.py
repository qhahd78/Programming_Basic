# 리스트의 메서드를 사용하여 단어의 개수를 리턴하는 함수 
def wCount(word):
    wlist = []
    # text 변수의 내용을 공백 문자를 기준으로 분리하여 리스트를 생성 
    for wd in text.split():
        # 분리된 내용을 wlist 에 append 
        wlist.append(wd)
    
    # 생성된 리스트의 개수를 세어 리턴한다. 
    cnt = wlist.count(word)
    return cnt

# 파일 열기 
f = open("Imagine.txt")
# 파일을 읽어 변수에 저장 
text = f.read()

# 단어 선택 
w = "Imagine"
# 함수 호출 (검색할 단어 Imagine으로 설정)
n = wCount(w) 
print(w + ":" + str(n)) # 단어 개수 출력 

# 복수의 단어 카운트 
wlist = ["Imagine", "people", "dreamer"]
# 빈 딕셔너리 생성
s = {}

# 단어가 key, 개수가 value 로 딕셔너리에 저장 
for wd in wlist : 
    # 함수를 호출하여 리턴값을 저장. 
    n = wCount(wd)
    s[wd] = n

print(s)