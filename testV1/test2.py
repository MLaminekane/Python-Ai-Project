from tkinter import *
import datetime

root = Tk()

def envoie():
  envoie = "User: " + e.get()
  txt.insert(END, "\n" +envoie)


  e.delete(0, END)



txt = Text(root, font=("times new roman", 15))
txt = Text(root)
txt.grid(row=0, column=0, columnspan=4)
e = Entry(root, width=100)
e.grid(row=1, column=0)
envoyer = Button(root, text="Send", command=envoie).grid(row=1, column=1)

root.title("MLK")
root.mainloop()