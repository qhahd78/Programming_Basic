# 의용메카트로닉스공학과 20195277 하유민 
print("의용메카트로닉스공학과 20195277 하유민")

from tkinter import *
import tkinter.messagebox

def save_data() : 
    try:
        fileD = open("deliveries.txt","a")
        fileD.write("Depot:\n")
        fileD.write("%s\n" % depot.get())
        fileD.write("Description:\n")
        fileD.write("%s\n" % description.get())
        fileD.write("Address:\n")
        fileD.write("%s\n" % address.get("1.0", END))
        depot.set(None)
        description.delete(0, END)
        address.delete("1.0", END)
    except Exception as ex:
        tkinter.messagebox.showerror("Error!", "Can't write to the file\n %s" % ex)
def read_depots(file): 
    depots = []
    depots_f = open(file)
    for line in depots_f:
        depots.append(line.rstrip()) # 줄바꿈 제거 
    return depots

app = Tk()
app.title("Head-Ex Dliveries")

Label(app, text="Depot:").pack()
depot = StringVar()
depot.set(None)
options = read_depots("depots.txt")
OptionMenu(app, depot, *options).pack()

Label(app, text="Description:").pack()
description = Entry(app)
description.pack()

Label(app, text = "Address:").pack()
address = Text(app)
address.pack()

Button(app, text="Save", command = save_data).pack()
app.mainloop()