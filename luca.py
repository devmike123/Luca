# :copyright: (c) 2019-present Aniket Bhattacharjee 
# :license: MIT, see LICENSE for more details.

import pyttsx3
import speech_recognition as sr
import datetime
import os
import wikipedia
from requests import get
import webbrowser
import sys
import pywhatkit
from bs4 import BeautifulSoup
import requests
import pywikihow
from pywikihow import search_wikihow

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
print(voices[0].id)
engine.setProperty('voices', voices[0].id)

def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()

def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source,timeout=10,phrase_time_limit=30)

        try:
            print("Recognizing...")
            query = r.recognize_google(audio, language= 'en-in')
            print(f"User Said: {query}")

        except Exception as e:
            speak("Sir can you please repeat...")
            return "none"
        return query

def wish():
    hour = int(datetime.datetime.now().hour)
    specimen = datetime.datetime.now().strftime('%I:%M %p')

    if hour>=0 and hour<=12:
        speak(f"Good Morning Sir its {specimen}")
    elif hour>12 and hour<10:
        speak(f"Good Afternoon Sir its {specimen}")
    else:
        speak(f"Good Evening Sir its {specimen}")
    speak("How can i help")
    




if __name__ == "__main__":
    wish()
    while True:

        query = takecommand().lower()

        if "wikipedia" in query:
            speak("Searching for the results in Wikipedia...")
            query = query.replace("wikipedia","")
            results = wikipedia.summary(query, sentences=2)
            speak("According to wikipedia")
            speak(results)
         

        elif "google" in query:
            speak("Sir what should i search in google")
            cm = takecommand().lower()
            webbrowser.open("www.google.com/search?q=" + cm)

        
            
        elif "go to sleep" in query:
            speak("Ok sir have a good day")
            sys.exit()

        elif "time now" in query:
            global time
            time = "The time is " +  datetime.datetime.now().strftime('%I:%M %p')
            speak(time)

        elif "temperature in" in query:
            search = query.replace("temperature in","")
            url = f"https://www.google.com/search?q={search}"
            r = requests.get(url)
            data = BeautifulSoup(r.text, "html.parser")
            temp = data.find("div" ,class_="BNeawe").text
            weather = f"Currently in {search} it is {temp} with hazz"
            speak(weather)
            sys.exit()


        elif "play" in query:
            song = query.replace('play', '')
            speak('playing ' + song)
            pywhatkit.playonyt(song)
            sys.exit()
            
        elif "stop" in query:
            print("Program Terminated")
            speak("Hope you had a wonderful time")
            sys.exit()

        elif "no thanks" in query:
            print("Program Terminated")
            speak("Hope you had a wonderful time")
            sys.exit()

        elif "date" in query:
            date = datetime.datetime.now().strftime('%d %B %Y')
            speak(f"Today's date is {date}")

        elif "news" in query:
            speak("Here is the latest news")
            webbrowser.open("https://news.google.co.in/")
            sys.exit()
        elif "how" in query:
            speak(" i am opening a video which can help you")
            pywhatkit.playonyt(query)
            speak("thank you")
            sys.exit()

        elif "flip a coin" in query:
            speak("fliping a coin")
            webbrowser.open("https://www.google.com/search?q=flip+a+coin")
            sys.exit()


        else:
            sir = query.replace("ok luca", "")
            webbrowser.open("www.google.com/search?q=" + sir)
            results = wikipedia.summary(query, sentences=2)
            speak("According to wikipedia")
            speak(results)
            sys.exit()


            

    
