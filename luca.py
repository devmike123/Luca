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
        audio = r.listen(source,timeout=10,phrase_time_limit=50)

        try:
            print("Recognizing...")
            query = r.recognize_google(audio, language= 'en-in')
            print(f"user said: {query}")

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

        elif "open youtube" in query:
            webbrowser.open("www.youtube.com")
            sys.exit()

        elif "search" in query:
            speak("Sir what should i search in google")
            cm = takecommand().lower()
            webbrowser.open("www.google.com/search?q=" + cm)

        elif "open whatsapp" in query:
            webbrowser.open("https://whatsapp.com/")
            sys.exit()

        elif "open twitter" in query:
            webbrowser.open("https://twitter.com/")
            sys.exit()

        
            
        elif "go to sleep" in query:
            speak("Ok sir have a good day")
            sys.exit()

        elif "time now" in query:
            global time
            time = "The time is " +  datetime.datetime.now().strftime('%I:%M %p')
            speak(time)

        elif "open mail" in query:
            webbrowser.open("https://mail.google.com/mail/u/0/#inbox")

        

        elif "set a reminder for tomorrow" in query:
            speak("what is the topic of the reminder")
            topic = takecommand().lower()
            speak("at what time do you want it to be reminded to you")
            momory = takecommand().lower()
            rescue = "Don't forget about" + topic + "" + "at" + momory

        elif "temperature" in query:
            search = "temperature in usa"
            url = f"https://www.google.com/search?q={search}"
            r = requests.get(url)
            data = BeautifulSoup(r.text, "html.parser")
            temp = data.find("div" ,class_="BNeawe").text
            weather = f"Currently in USA it is {temp} with hazz"
            speak(weather)
            speak(f"Today it will be partly sunny with a forcast tie of {temp}")

        elif "good morning" in query:
            speak("good morning sir")
            time = "The time is " +  datetime.datetime.now().strftime('%I:%M %p')
            speak(time)
            search = "temperature in usa"
            url = f"https://www.google.com/search?q={search}"
            r = requests.get(url)
            data = BeautifulSoup(r.text, "html.parser")
            temp = data.find("div" ,class_="BNeawe").text
            weather = f"Currently in USA it is {temp} with hazz"
            speak(weather)
            speak(f"Today it will be partly sunny with a forcast tie of {temp}")
            speak("opening whatsapp")
            webbrowser.open("https://web.whatsapp.com/")
            speak("playing senorita")
            pywhatkit.playonyt('senorita')
            speak("Have a good day sir")
            sys.exit()


        elif "play" in query:
            song = query.replace('play', '')
            speak('playing ' + song)
            pywhatkit.playonyt(song)
            sys.exit()
            
        elif "none" in query:
            print("none")

        elif "no thanks" in query:
            print("none")

        elif "translate" in query:
            webbrowser.open("https://translate.google.co.in/")
            sys.exit()

        elif "date" in query:
            date = datetime.datetime.now().strftime('%d %B %Y')
            speak(f"Today's date is {date}")

        elif "what is your name" in query:
            speak("Just a rather very interesting system")
            speak(" in short jarvis you can simply call me jarvis")

        elif "how old are you" in query:
            speak(" i am very old to use internet but i am very young to sing a song")

        elif "what is my name" in query:
            speak("your name is Mike")

        elif "news" in query:
            speak("Here is the latest news")
            webbrowser.open("https://news.google.co.in/")
            sys.exit()
        
        elif "wake up" in query:
            speak("Good morning Mike")
            music_dir = "C:\\Users\\xyz\\Desktop\\Google\\iPad Pro — Float.mp4"
            os.startfile(music_dir)
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


            

    
