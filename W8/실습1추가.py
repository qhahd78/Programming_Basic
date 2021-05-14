# 의용메카트로닉스공학과 20195277 하유민 
print("의용메카트로닉스공학과 20195277 하유민")

from tkinter import *

def save_data() : 
    fileD = open("deliveries.txt","a")
    fileD.write("Depot:")
    fileD.write("%s\n" % depot.get())
    fileD.write("Description:")
    fileD.write("%s\n" % description.get())
    fileD.write("Address:")
    fileD.write("%s\n" % address.get("1.0", END))
    fileD.write("택배기사:")
    fileD.write("%s\n" % deliver.get())
    depot.delete(0, END)
    description.delete(0, END)
    address.delete("1.0", END)
    deliver.delete(0, END)

app = Tk()
app.title("Head-Ex Deliveries")

Label(app, text = "Depot:").pack()
depot = Entry(app)
depot.pack()

Label(app, text = "Description:").pack()
description = Entry(app)
description.pack()

Label(app, text="Address:").pack()
address = Text(app)
address.pack()

Label(app, text="택배기사:").pack()
deliver = Entry(app)
deliver.pack()

Button(app, text = "Save", command = save_data).pack()

app.mainloop()