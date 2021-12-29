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
        speak("Hello Adi,Good Morning")
        print("Hello Adi,Good Morning")
    elif hour>=12 and hour<15:
        speak("Hello Adi,Good Afternoon")
        print("Hello Adi,Good Afternoon")
    else:
        speak("Hello Adi,Good Evening")
        print("Hello Adi,Good Evening")

wishTime()
