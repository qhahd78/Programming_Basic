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

# 검색하고 싶은 surfer 의 id 를 입력 받는다. 
lookup_id = int(input("Enter the id of the surfer: "))

# find_details 함수를 실행하여 lookup_id 와 맞는 surfer 를 찾는다. 
surfer = find_details(lookup_id)
    
# surfer를 찾았다면 surfer의 정보를 print 한다. 
if surfer: 
    print("ID:      " + surfer['id'])
    print("Name:      " + surfer['name'])
    print("Country:      " + surfer['country'])
    print("Average:      " + surfer['average'])
    print("Board type:      " + surfer['board'])
    print("Age:      " + surfer['age'])    