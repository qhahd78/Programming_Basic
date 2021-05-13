from tkinter import * 
counter = 0 # counter 변수 선언 및 초기화 

def counter_label(label): # 함수 counter_label()
    def count(): # 함수 count()
        global counter # 전역변수 counter 
        counter += 1 # count 증가 
        # text 속성 변경 
        label.config(text=str(counter))
        label.after(1000, count)
    count() # 카운트 함수 호출 

app = Tk()
app.title("Counting Seconds")
label = Label(app, fg="green") # 글자색 녹색 
label.pack()
counter_label(label) # counter_label 호출 
button = Button(app, text="Stop", width=25, command=app.destroy)
button.pack()
app.mainloop()