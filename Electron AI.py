import pyttsx3
import pyaudio
import datetime
import wikipedia
import speech_recognition as sr 
import os
import webbrowser
#import google
import random
engine = pyttsx3.init()
voices = engine.getProperty("voices")
#print(voices[0].id)
engine.setProperty("voices", voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning")
    elif hour>=12 and hour<17:
        speak("Good Afternoon")
    elif hour>=17 and hour<20:
        speak("Good Evening")
    else:
        speak("this is night but its not over we will work till midnight")
    
    speak("I am electron, please tell me what I can do for you")
    
    
def takeCommand():
    '''It takes microphone input from the user and returns string output'''

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening......")
        r.pause_threshold= 1
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)

    try:
        print("Recognising......")
        query = r.recognize_google(audio)
        print(f"User said: {query}\n")
    
    except Exception as e:
        #print(e)			
        #speak("Sorry i didnt understand say that again please")
        print("Say that again please......")
        return "None"
    '''query = str(input("Please input your command to electron here: e"))'''
    return query



if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()

        if "electron" in query:
            speak("yes sir")
        

            '''Logic for executing tasks based on query'''
            
            if "wikipedia" in query:
                speak("Searching Wikipedia....")

                query = query.replace("Wikipedia","")

                results = wikipedia.summary(query, sentences = 2)
                speak("According to Wikipedia")
                speak(results)
                
            elif "play music" in query:
                music_dir="D:\\Fun Stuff\\Music"
                songs = os.listdir(music_dir)
                #print("Play songs",songs)
                os.startfile(os.path.join(music_dir, songs[random.randint(1,188)]))
            
            elif "open google" in query:
                webbrowser.open("google.com")
            
            elif "open youtube" in query:
                webbrowser.open("youtube.com")
            
            elif "open ocean of games" in query:
                webbrowser.open("oceanofgames.com")
            
            elif "the time" in query:
                strTime = datetime.datetime.now().strftime("%H:%M:%S")
                speak(f"Sir, the time is {strTime}")
            
            elif "hello" in query:
                speak("hello, its good to talk to you")

            elif "how to satisfy a monstor" in query:
                speak("give her a party every single second")
            
            elif "you are good" in query:
                speak("thats really nice of you to say, thank you")
            
            elif "open spotify" in query:
                #spotifyPath = "C:\\Users\\angad\\AppData\\Local\\Microsoft\\WindowsApps\\spotify"
                spotifyPath = "C:\\Users\\angad\\AppData\\Roaming\\Spotify.exe"
                os.startfile(spotifyPath)

            elif "open code" in query:
                codePath="C:\\Users\\angad\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
                os.startfile(codePath)
            

            elif "open grand theft auto" in query:
                gtapath="D:\\Fun Stuff\\New folder\\Grand Theft Auto V\\PlayGTAV.exe"
                os.startfile(gtapath)
            
            elif "open discord" in query:
                discorpath="C:\\Users\\angad\\AppData\\Local\\Discord\\app-0.0.309\\Discord.exe"
                os.startfile(discorpath)
            
            elif "open chrome" in query:
                chromepath="C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
                os.startfile(chromepath)

            elif "wake up" in query:
                speak("i am up and running sir")
            
            elif "how are you" in query:
                speak("i am really good, thanks for asking")
                
            elif "google" in query:
                speak("Searching google....")

                query = query.replace("google","")

                results = google.summary(query, sentences = 2)
                speak("According to google")
                speak(results)
            
            elif "how can you help me" in query:
                speak("I am here to entertain you")

            elif "where do you live" in query:
                speak("i live in the universe")
            
            elif "what do you like to eat" in query:
                speak("i like to eat mango")
            
            elif "what is our national fruit" in query:
                speak("Our national fruit is mango")

            elif "what is our national tree" in query:
                speak("Our national tree is banyan tree")

            elif "open virtual machines" in query:
                vmwarepath ="E:\\SENECA\\Summer Semester\\MST 100 NDD\\Software install\\VM workstation"
                os.startfile(vmwarepath)

            
        elif "shutdown" in query:
            speak("shatting down")
            break
