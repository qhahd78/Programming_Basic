#의용메카트로닉스공학과 20195277 하유민
print("의용메카트로닉스공학과 20195277 하유민")

from tkinter import * 
import pygame.mixer 
import tkinter.messagebox

app=Tk()
app.title("Head First Mix")
app.geometry("250x100+200+100")

sound_file = "50459_M_RED_Nephlimizer.wav"

mixer = pygame.mixer 
mixer.init()

def track_start(): 
    track.play(loops= -1)

def track_stop():
    track.stop()

def shutdown():
    track.stop()
    tkinter.messagebox.askquestion("안녕?", "정말로 종료하시겠어요?")
    app.destroy()
    

track=mixer.Sound(sound_file)

start_button = Button(app,command = track_start, text= "Start")
start_button.pack(side = LEFT)
stop_button = Button(app, command= track_stop, text = "Stop")
stop_button.pack(side = RIGHT)
app.protocol("WM_DELETE_WINDOW", shutdown)
app.mainloop()