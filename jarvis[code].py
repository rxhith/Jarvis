import datetime
import random
import pyjokes

import speech_recognition as sr
import mlphon as  m

import pyttsx3
import os
import smtplib
import wikipedia
import webbrowser

engine = pyttsx3.init('sapi5')
voices= engine.getProperty('voices') #getting details of current voice
engine.setProperty('voice', voices[1].id)
engine.setProperty('rate', 100)



def speak(audio):
       
     engine.say(audio) 
     engine.runAndWait() #Without this command, speech will not be audible to us.      #For now, we will write the conditions later.


def wishme():
     speak("HI MASTER")
     """speak("Hi, I'm Chitti the Robot. Speed 1 terahertz, memory 1 zigabyte.")
     speak("My motto is NO WAR ONLY LOVE")
     speak("Shall we begin, my love?")
     speak("the time is")
     hour = int(datetime.datetime.now().hour)
     speak(hour)
     speak("hours")
     min = int(datetime.datetime.now().minute)
     speak(min)
     speak("minutes")"""



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

    except Exception as e:
        # print(e)    
        print("Say that again please...")   #Say that again will be printed in case of improper voice 
        return "None" #None string will be returned
    return query

 
def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('youremail@gmail.com', 'your-password')
    server.sendmail('youremail@gmail.com', to, content)
    server.close()


  


if __name__ == "__main__":
    wishme()
    speak("code with rohith")
    while True:
    # if 1:
        query = takeCommand().lower() #Converting user query into lower case
        if 'alexa' in query:
            speak('What do you want')
            query = takeCommand().lower()


        # Logic for executing tasks based on query
            if 'wikipedia' in query:  #if wikipedia found in the query then this block will be executed
                speak('Searching Wikipedia...')
                speak("What to search")
                query = takeCommand().lower()
                #query = query.replace("wikipedia", "")
                webbrowser.open("https://en.wikipedia.org/wiki/"+query)
                results = wikipedia.summary(query, sentences=2) 
                speak("According to Wikipedia")
                print(results)
                speak(results)
            elif 'open youtube' in query:
                webbrowser.open("https://www.youtube.com")
            elif 'open google' in query:
                webbrowser.open("https://www.google.com")
            elif 'play music' in query:
                music_dir = 'C:\\Users\\ROHITH SYAM\\Dropbox\\My PC (LAPTOP-IH3AR4SQ)\\Desktop\\Jarvis Project'
                songs = os.listdir(music_dir)
                #song_index = random.randint(0, len(songs) - 1) # Generate a random index value
                for i in range(0,len(songs)):
                    print(20+i)
                    print(songs[i])
                speak("tell the song number")
                query = takeCommand().lower()
                while query=="none":
                    speak("Can You Repeat")
                    query = takeCommand().lower()
                song_index2=int(query)-20
                #print(songs)    
                os.startfile(os.path.join(music_dir, songs[song_index2]))
            elif 'the time' in query:
                strTime = datetime.datetime.now().strftime("%H:%M:%S")    
                speak(f"Sir, the time is {strTime}")
            elif 'open code' in query:
                codePath = "C:\\Users\\Haris\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
                os.startfile(codePath)
            elif 'email to harry' in query:
                try:
                    speak("What should I say?")
                    content = takeCommand()
                    to = "harryyourEmail@gmail.com"    
                    sendEmail(to, content)
                    speak("Email has been sent!")
                except Exception as e:
                    print(e)
                    speak("Sorry cant send")
            elif 'close' in query:
                speak("Closing, Bye")
                break    
            elif 'search youtube' in query:
                speak("What to search")
                query = takeCommand().lower()
                webbrowser.open("https://www.youtube.com/results?search_query="+query)
            elif 'search spotify' in query:
                speak("What to search")
                query = takeCommand().lower()
                while query=="none":
                    speak("Can You Repeat")
                    query = takeCommand().lower()
                webbrowser.open("https://open.spotify.com/search/"+query)
            elif 'search news' in query:
              
                webbrowser.open("https://www.bbc.com/")
            elif 'tell a joke' in query:
                speak(pyjokes.get_joke())
            elif 'search' in query:
                speak("What to search")
                query = takeCommand().lower()
                webbrowser.open("https://www.google.com/search?q="+query)
      

            
            
            
                
