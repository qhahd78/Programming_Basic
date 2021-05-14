# 의용메카트로닉스공학과 20195277 하유민 
print("의용메카트로닉스공학과 20195277 하유민")

from tkinter import *

def save_data() : 
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

app = Tk()
app.title("Head-Ex Deliveries")

Label(app, text = "Depot:").pack()
depot = StringVar()
depot.set(None)

# 같은 그룹에서는 한 가지만 고를 수 있게 된다. 
Radiobutton(app, variable=depot, text="Cambridge, MA", value="Cambridge, MA").pack()
Radiobutton(app, variable=depot, text="Cambridge, UK", value="Cambridge, UK").pack()
Radiobutton(app, variable=depot, text="Seattle, WA", value="Seattle, WA").pack()

Label(app, text = "Description:").pack()
description = Entry(app)
description.pack()
Label(app,text="Adress:").pack()
address=Text(app)
address.pack()

Button(app, text = "Save", command = save_data).pack()

app.mainloop()
