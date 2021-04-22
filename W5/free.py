# 빈 리스트 wordlist 생성
wordlist = []

# 파일을 열고 text에 내용을 저장한다. 
f = open("free.txt", 'r', encoding='UTF-8')
text = f.read()

# 공백을 기준으로 글자들을 나눠 wordlist 에 저장한다. 
for wd in text.split(): 
    wordlist.append(wd)

# 검색하고 싶은 단어를 입력 받아 searchword 에 저장한다. 
searchword = input("검색할 단어를 입력하세요. ")
# count 변수를 선언해준다. 
count = 0 

# wordlist 를 한 바퀴 돌면서 아래의 코드를 실행한다. 
for wd in wordlist : 
    # 만약 wordlist 안에 있는 단어와 searchword 가 일치한다면 count를 1씩 증가시킨다. 
    if wd == searchword: 
        count = count + 1

# searchword 가 나온 수만큼 증가된 count 값을 출력한다. 
print('해당 단어는 이 텍스트 문서에서 %d 번 나왔습니다.'%count)