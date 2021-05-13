from tkinter import * # tkinter 모듈 불러오기 
import pygame.mixer 

sounds = pygame.mixer
sounds.init()
correct_s = sounds.Sound("correct.wav")
wrong_s = sounds.Sound("wrong.wav")

number_correct = 0
number_wrong = 0 

def play_correct_sound(): 
    global number_correct # 광역 변수  
    number_correct = number_correct + 1
    correct_s.play()

def play_wrong_sound():
    global number_wrong
    number_wrong = number_wrong + 1
    wrong_s.play()

app = Tk() # 윈도우 생성 
app.title("TVN Game show") # 윈도우 이름(title) 설정 
app.geometry("300x110+200+100") # 윈도우 좌표, 크기를 설정 

b1 = Button(app, text = "Correct!", width =10, command = play_correct_sound) # 버튼을 윈도우에 추가, command 인자로 실행할 함수 이름 지정 
b1.pack(side = 'left', padx = 10, pady = 10) # 버튼을 윈도우에 연결 

b2 = Button(app, text = "Wrong!", width = 10, command = play_wrong_sound)
b2.pack(side = 'right', padx = 10, pady = 10)

app.mainloop() # tkinter 이벤트 루프 시작 

print(str(number_correct)+"were correctly answered.")
print(str(number_wrong)+"were answered incorrectly.")