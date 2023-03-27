import pyttsx3
import datetime
import speech_recognition as sr
from speech_recognition import Recognizer
import wikipedia
import webbrowser
import os


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices[1].id)
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()
    
def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("goodmorning arpit , namaste,have a nice day")
    elif hour>=12 and hour<16:
        speak("goodafternoon arpit,do your lunch")
    elif hour>=15 and hour<19:
        speak("good evening arpit,have a sip of coffee")
    elif hour>=20 and hour<22 :
        speak("do your  dinner ")
    else :
        speak ("goodnight arpit and sweetdreams")
        
def takecommand():
    #it take microphone input from the user and returns string output
    r = sr.Recognizer()
    with sr.Microphone()as source:
        print("Listening")
        r.pause_threshold = 1
        audio = r.listen( source)
    try:
        print("Recognizing....")
        query = r.recognize_google(audio,language ="en-in")    
        print(f"user said:{query}\n")
    
    except Exception as e :
        print(e)
        print("say that again please....")
        return "None"
    
    return query

if __name__ =="__main__":
    wishme()
    while True:
     query = takecommand().lower()
     
     #logic for executing task based on query
     if 'wikipedia' in query:
         speak("searching wikipedia....")
         query = query.replace("wikipedia","")
         results = wikipedia.summary(query,sentences=2)
         speak("according to wikipedia")
         print(results)
         speak(results)
        
     elif 'open youtube' in query:
         webbrowser.open("youtube.in")
     elif 'open google' in query:
         webbrowser.open("www.google.com")
     elif 'open instagram' in query:
         webbrowser.open("www.instagram.com")
     elif 'play music' in query :
          music_dir= 'c:\\songs'
          songs = os.listdir(music_dir)
          print(songs)
          os.startfile(os.path.join(music_dir, songs[1]))
     elif 'the time ' in query:
         starttime= datetime.datetime.now().strftime("%H:%M:%S")
         speak(f"sir,the time is {starttime}")
          
     elif "open code " in query:
         path = "C:\\Users\\arpit\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs"
         os.startfile(path)
         
         
         
         
    
    
    
    