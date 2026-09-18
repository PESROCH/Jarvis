from playsound import playsound
import speech_recognition as sr
import pyaudio
import os
import time
import random
import webbrowser
from datetime import datetime

micindex = None

folpok = "voice/ok"
folpbye = "voice/bye"
folphi = "voice/hi"

r = sr.Recognizer()
r.dynamic_energy_threshold = True
r.energy_threshold = 3750

tim = ["сколько время", "который час", "время", "сколько сейчас времени"]
search = ["найди про", "найди", "ищи", "что такое", "кто такие", "кто такой"]
search_video = ["найди видео про", "ищи видео про", "кто такой", "кто такие"]
open_browser = ["браузер", "открой браузер", "интернет"]
open_youtube = ["ютуб", "открой ютуб", "youtube"]
bye = ["пока", "до свидания", "до завтра"]
hi = ["джарвис", "привет", "добрый день"]

for index, name in enumerate(sr.Microphone.list_microphone_names()):
    if name == "РњРёРєСЂРѕС„РѕРЅ (Usb Audio Device)":
        micindex = index
        break

with sr.Microphone(device_index = micindex) as source:
    r.adjust_for_ambient_noise(source, duration = 2)

while True:
    try:
        with sr.Microphone(device_index = micindex) as source:
            audio = r.listen(source)
            text = r.recognize_google(audio, language = "ru-RU")
            text = text.lower()

        currtrigger = None

        for trigger in search:
            if text.startswith(trigger):
                currtrigger = trigger
                break

        if currtrigger is not None:
            query = text.replace(currtrigger, "", 1).strip()

            if query:
                allmp3 = os.listdir(folpok)
                openq = random.choice(allmp3)
                playsound(os.path.join(folpok, openq))
                webbrowser.open(f"https://www.google.com/search?q={query}")

        if text in tim:
            now = datetime.now()
            currtime = now.strftime("%H:%M")
            print(f"время сейчас: {currtime}")
            playsound("voice/time/time.mp3")
        
        if text in hi:
            allmp3 = os.listdir(folphi)
            hello = random.choice(allmp3)
            playsound(os.path.join(folphi, hello))

        if text in open_browser:
            allmp3 = os.listdir(folpok)
            openb = random.choice(allmp3)
            playsound(os.path.join(folpok, openb))
            webbrowser.open("https://www.google.com")

        if text in open_youtube:
            allmp3 = os.listdir(folpok)
            openb = random.choice(allmp3)
            playsound(os.path.join(folpok, openb))
            webbrowser.open("https://youtube.com")

        currtrigger_v = None

        for trigger in search_video:
            if text.startswith(trigger):
                currtrigger_v = trigger
                break

        if currtrigger_v is not None:
            query = text.replace(currtrigger_v, "", 1).strip()

            if query:
                allmp3 = os.listdir(folpok)
                openq = random.choice(allmp3)
                playsound(os.path.join(folpok, openq))
                webbrowser.open(f"https://www.youtube.com/results?search_query={query}")

        if text in bye:
