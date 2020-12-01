import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os

engine = pyttsx3.init('sapi5')
voices= engine.getProperty('voices') #getting details of current voice
engine.setProperty('voice', voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def Greeting():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")
    elif hour>=12 and hour<=18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")
    speak("Hello! I am RichieRich. I am here to help you in your daily tasks.How can I help you?")

def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in') #Using google for voice recognition.
        print(f"User said: {query}\n")  #User query will be printed.

    except Exception:
        # print(e)    
        print("Say that again please...")   #Say that again will be printed in case of improper voice 
        return "None" #None string will be returned
    return query


if __name__ == "__main__":
    q = True
    Greeting()
    while q:
        query = takeCommand().lower()

        # Logic for executing tasks 
        if 'wikipedia' in query:
            speak("Searching wikipedia...")
            query = query.replace("wikipedia" , "")
            result = wikipedia.summary(query , sentences=2)
            speak("Acoording to Wikipedia:")
            print(result)
            speak(result)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
        
        elif 'open google' in query:
            webbrowser.open("google.com")
        
        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")

        elif 'open github' in query:
            webbrowser.open("github.com")

        elif 'the time' in query:
            curr_Time = int(datetime.datetime.now().hour)
            speak(f"The current time is:{curr_Time}")    

        elif 'open code' in query:
            codePath = "C:\\Users\\PREETI\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)
        
        elif 'open word' in query:
            wordPath = "C:\\Program Files\\Microsoft Office\\root\\Office16\\WINWORD.EXE"
            os.startfile(wordPath)

        elif 'open powerpoint' in query:
            pointPath = "C:\\Program Files\\Microsoft Office\\root\\Office16\\POWERPNT.EXE"
            os.startfile(pointPath)

        elif 'open notes' in query:
            notePath = "C:\\Program Files\\Microsoft Office\\root\\Office16\\ONENOTE.EXE"
            os.startfile(notePath)

        elif 'bye' in query:
            q = False

    speak("Bye!Hope I helped you . Have a nice Day! ")
        

        


        
        

        



                        
        



