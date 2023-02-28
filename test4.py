API_KEY = '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'
import openai
import os
os.environ['OPENAI_Key'] = API_KEY
openai.api_key = os.environ['OPENAI_Key']
from tkinter import *
root = Tk()
def envoie(event=None):
    prompt = e.get()
    response = openai.Completion.create(engine='text-davinci-003', prompt=prompt, max_tokens=256)
    reponse_text = response['choices'][0]['text']
    envoie = "User: " + prompt + "\n" + "MLK: " + reponse_text
    txt.insert(END, envoie)
    e.delete(0, END)
txt = Text(root, font=("times new roman", 15))
txt.grid(row=0, column=0, columnspan=4)
e = Entry(root, width=100)
e.grid(row=1, column=0)
e.bind("<Return>", envoie)
envoyer = Button(root, text="Send", command=envoie).grid(row=1, column=1)
root.title("MLK")
root.mainloop()