import pyttsx3
from datetime import datetime
import speech_recognition as sr 
from wikipedia import summary as wiki_summary
from webbrowser import open as web_open
from os import listdir as os_listdir
from os import startfile as os_startfile
from os import path as os_path

engine = pyttsx3.init("sapi5") 
voices = engine.getProperty('voices') 
engine.setProperty('voices', voices[0].id)

def speak(audio) : 
    engine.say(audio) 
    engine.runAndWait()
    
def wishMe() : 
    hour = int(datetime.now().hour)
    if hour < 12 : 
        speak("Good Morning!") 
    elif hour < 18 : 
        speak("Good Afternoon!") 
    else : 
        speak("Good Evening!") 
    speak("I am your Voice Assistent Sir, Please tell me how can i help you?")
    
def takeCommand() : 
    '''
    It takes microphone input from the user and return string output
    '''
    r = sr.Recognizer() 
    with sr.Microphone() as source :
        print("Listening...") 
        r.pause_threshold = 1
        audio = r.listen(source) 
        
    try : 
        print("Recognizing...") 
        query = r.recognize_google(audio_data=audio, language='en-in')
        print("User Said:", query) 
    except Exception as e : 
        print(e)
        print('Say that again please...') 
        return "None"
    return query

if __name__ == '__main__' :
    wishMe()
    while True : 
        query = takeCommand().lower()
        
        if "wikipedia" in query : 
            print("Searching Wikipedia...")
            speak("Searching Wikipedia") 
            query = query.replace("wikipedia", '')
            results = wiki_summary(query, sentences=2) 
            speak("According to Wikipedia") 
            speak(results)
        
        elif "open youtube" in query : 
            web_open("youtube.com") 
        
        elif "open google" in query : 
            web_open("google.com") 
            
        elif "play music" in query: 
            music_dir = "C:\\Users\\arksi\\Music"
            songs = os_listdir(music_dir) 
            print(songs) 
            os_startfile(os_path.join(music_dir, songs[0]))
            
        elif "the time" in query : 
            strTime = datetime.now().strftime("%H:%M:%S") 
            speak(f"sir, the time is {strTime}") 
            
        elif "open code" in query : 
            os_startfile(r"C:\Users\arksi\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Visual Studio Code\Visual Studio Code.lnk")
            
        elif "turn off" in query : 
            speak("ok sir, have a nice day")
            break 
            
        else : 
            speak("Not able to understand. Can you repeat your statement, sir.")
            