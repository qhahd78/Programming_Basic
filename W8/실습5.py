# 의용메카트로닉스공학과 20195277 하유민 
print("의용메카트로닉스공학과 20195277 하유민")

from tkinter import *

app = Tk()
app.title("그리드 테스트")
colours = ['red', 'green', 'orange', 'white', 'yellow', 'blue']

r = 0 
for c in colours: 
    Label(app, text=c, relief="ridge", width=20).grid(row=r, column=0)
    Entry(app, bg=c, relief="sunken", width=30).grid(row=r, column=1)
    r = r+1

app.mainloop()