from tkinter import *
from PIL import ImageTk, Image
import os

def clicked(i):
    topImg = PhotoImage(file=str(i)+".png")
    panel.configure(image=topImg)
    panel.image = topImg

root = Tk()
root.geometry("1000x1000")
img = ImageTk.PhotoImage(Image.open("0.png"))

panel = Label(root, image = img)
panel.grid(column=0, row=0)
for i in range(5):
    btn = Button(root, text="Повторить", command=lambda: clicked(i))
btn.grid(column=0, row=1)
#panel.pack(side = "bottom", fill = "both", expand = "yes")
root.mainloop()