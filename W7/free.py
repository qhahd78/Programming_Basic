from tkinter import *

final = ""


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

app = Tk()
app.title("입력 받고 출력하기")
# 안내 문구 
lab1 = Label(app, text="학과 이름 학번을 입력해보세요. ",fg="blue")
lab1.pack()

# 학과 문구 
lab2 = Label(app, text="학과")
lab2.pack()
# 학과 입력 받기 
input_dep = StringVar() # StringVar 설정
dep = Entry(app, textvariable=input_dep) 
dep.pack()

# 이름 문구 
input_name = StringVar()
label = Label(app, text="이름")
label.pack()
# 이름 입력 받기 
name = Entry(app, textvariable=input_name)
name.pack()

# 학번 문구 
lab3 = Label(app, text="학번")
lab3.pack()

# 학번입력 받기 
input_num = StringVar()
num = Entry(app, textvariable=input_num)
num.pack()

# 버튼을 누르면 input_info 함수 실행 
btn = Button(app, text="print 하기", command=input_info)
btn.pack()

# label 로 입력 받은 값들을 텍스트로 출력하기 
result1 = Label(app, textvariable = input_dep)
result1.pack()

result2 = Label(app, textvariable = input_name)
result2.pack()

result3 = Label(app, textvariable = input_num)
result3.pack()




app.mainloop()