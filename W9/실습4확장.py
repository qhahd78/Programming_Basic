from tkinter import * 
import tkinter.messagebox as mb 
from tkinter import filedialog as fd 

app = Tk()
app.title("Head First Mix")
app.geometry("250x100+200+100")

sound_file="50459_M_RED_Nephlimizer.wav"

mixer = pygame.mixer 
mixer.init()

def track_toggle():
    if track_playing.get() ==1:
        track.play(loops=-1)
    else: 
        track.stop()

def shutdown():
    track.stop()
    app.destroy()

def callback(): 
    global track
    name = fd.askopenfilename()
    track=mixer.Sound(name)


Button(app, text='파일오픈', command=callback).pack(side='bottom')
app.mainloop()