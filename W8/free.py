#의용메카트로닉스공학과 20195277 하유민 
print("의용메카트로닉스공학과 20195277 하유민")

from tkinter import *

# 받은 값을 print 해주는 함수 
def input_info(): 
    # global final

    final = StringVar()

    # get method 로 입력한 값들을 가져온다. 
    dep1 = input_dep.get()
    name1 = input_name.get()
    num1 = input_num.get()

    # 학과, 이름, 학번을 한 줄로 출력하기 위해 final 변수 선언 
    final= dep1+name1+num1

    # 학과, 이름, 학번을 한 줄로 출력해준다. 
    print(final)

    return   

# save_data() 함수 정의 
def save_data(): 
    TextFile = open("free.txt", "a")
    TextFile.write("[입력받은 사람의 정보]\n")
    TextFile.write("학과: ")
    TextFile.write("%s\n" % dep.get())
    TextFile.write("학번: ")
    TextFile.write("%s\n" % num.get())
    TextFile.write("이름: ")
    TextFile.write("%s\n" % name.get())

app = Tk()
app.title("입력 받고 출력하기 + 저장하기")
# 안내 문구 
lab1 = Label(app, text="학과 이름 학번을 입력해보세요. ",fg="blue").grid(row=0, column=0, columnspan=2)

# 학과 문구 
lab2 = Label(app, text="학과", width=20)
lab2.grid(row=1, column=0)
# 학과 입력 받기 
input_dep = StringVar() # StringVar 설정
dep = Entry(app, textvariable=input_dep, width=20) 
dep.grid(row=1, column=1)

# 이름 문구 
input_name = StringVar()
label = Label(app, text="이름",width=20)
label.grid(row=2, column=0)
# 이름 입력 받기 
name = Entry(app, textvariable=input_name, width=20)
name.grid(row=2, column=1)

# 학번 문구 
lab3 = Label(app, text="학번", width=20)
lab3.grid(row=3, column=0)

# 학번입력 받기 
input_num = StringVar()
num = Entry(app, textvariable=input_num, width=20)
num.grid(row=3, column=1)

# 버튼을 누르면 input_info 함수 실행 
btn = Button(app, text="print 하기", command=input_info, width=20)
btn.grid(row=7, column=0)

# 버튼을 누르면 save_data 함수 실행 
btn = Button(app, text="파일에 저장하기", command=save_data, width=20)
btn.grid(row=7, column=1)

# label 로 입력 받은 값들을 텍스트로 출력하기 
result1 = Label(app, textvariable = input_dep)
result1.grid(row=4, column=0, columnspan=2)

result2 = Label(app, textvariable = input_name)
result2.grid(row=5, column=0, columnspan=2)

result3 = Label(app, textvariable = input_num)
result3.grid(row=6, column=0, columnspan=2)

app.mainloop()