# 함수 정의 
def find_details(id2find):
    # csv 파일 열기 
    surfers_f = open("surfing_data.csv");
    for eachline in surfers_f: 
        s = {}
        (s["id"], s['name'], s['country'], s['average'], s['board'], s['age']) = eachline.split(";")
        # 만약 id 를 찾으면 
        if id2find == int(s['id']):
            # 파일을 닫고 
            surfers_f.close()
            # 이름을 리턴해준다. 
            return(s)
    surfers_f.close()
    # 없으면 빈 값 리턴 
    return({})

# while True 를 사용하여 -1 이 입력될 때까지 프로그램이 종료되지 않도록 한다. 
while True : 
    lookup_id = int(input("Enter the id of the surfer: "))
    surfer = find_details(lookup_id)
    
    

    if surfer: 
        print("ID:      " + surfer['id'])
        print("Name:      " + surfer['name'])
        print("Country:      " + surfer['country'])
        print("Average:      " + surfer['average'])
        print("Board type:      " + surfer['board'])
        print("Age:      " + surfer['age'])    

    # -1 이 입력될 경우, 프로그램을 종료한다. 
    if lookup_id == int(-1) : 
        print("끝")
        break