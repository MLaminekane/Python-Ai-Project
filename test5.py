import tkinter as tk
import speech_recognition as sr
import pyttsx3
import openai

openai.api_key = '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'

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voices', voices[1].id)

r = sr.Recognizer()
mic = sr.Microphone(device_index=1)

conversation = ""
user_name = "MLK"
bot_name = "MLK_Ai"

def start_listening():
    global conversation
    global mic
    global r

    with mic as source:
        print("\n POSEZ VOTRE QUESTION...")
        r.adjust_for_ambient_noise(source, duration=0.2)
        audio = r.listen(source)
    print("no longer listening")

    try:
        user_input = r.recognize_google(audio)
    except:
        return

    prompt = user_name+":"+user_input + "\n"+bot_name+":"
    conversation += prompt

    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=conversation,
        temperature=0.7,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )

    response_str = response["choices"][0]["text"].replace("\n", "")
    response_str =response_str.split(
        user_name + ":" ,1)[0].split(bot_name+ ":",1)[0]

    conversation+= response_str +"\n"
    print(response_str)

    engine.say(response_str)
    engine.runAndWait()

root = tk.Tk()
root.title("Assistant vocal")

question_label = tk.Label(root, text="Question :")
question_label.pack()

question_entry = tk.Entry(root, width=50)
question_entry.pack()

listen_button = tk.Button(root, text="Ecouter", command=start_listening)
listen_button.pack()

root.mainloop()
