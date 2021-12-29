import speech_recognition as sr
import pyttsx3
import datetime


engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice1','voices[0].id')

def speak(text):
    engine.say(text)
    engine.runAndWait()


def wishTime():
    hour=datetime.datetime.now().hour
    if hour>=0 and hour<12:
        speak("Hello _____,Good Morning")
        print("Hello _____,Good Morning")
    elif hour>=12 and hour<15:
        speak("Hello _____,Good Afternoon")
        print("Hello _____,Good Afternoon")
    else:
        speak("Hello _____,Good Evening")
        print("Hello _____,Good Evening")

wishTime()
