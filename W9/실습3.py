from tkinter import * 
import pygame.mixer

app = Tk()
app.title("Head First Mix")
sound_file="50459_M_RED_Nephlimizer.wav"
mixer = pygame.mixer
mixer.init()

def track_toggle(): 
    if track_playing.get() == 1: 
        track.play(loops=-1)
    else: 
        track.stop()

def change_volume(v): 
    # Scale 클래스 내에서 호출 시 인수 포함 
    # 스케일 값을 나타내는 인수 
    track.set_volume(volume.get())
    # track.set_volume(float(v))
def shutdown():
    track.stop()
    app.destroy()
track = mixer.Sound(sound_file)
track_playing = IntVar()
track_button = Checkbutton(app, variable = track_playing, command = track_toggle, text = sound_file)

track_button.pack(side=LEFT)

volume=DoubleVar()
volume.set(track.get_volume())
volume_scale=Scale(app, variable=volume, from_=0.0, to=1.0, resolution=0.1, command=change_volume, label="Volume", orient=HORIZONTAL)
volume_scale.pack(side=RIGHT)

app.protocol("WM_DELETE_WINDOW", shutdown)
app.mainloop()

