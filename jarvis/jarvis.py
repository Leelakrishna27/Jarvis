import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import pyaudio
import webbrowser as web
import os
import smtplib

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices[1].id)
engine.setProperty('voice',voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()
def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")
    elif hour>=12 and hour<16:
        speak("Good Afternoon")
    elif hour>=16 and hour<19:
        speak("Good Afternoon")
    else:
        speak("Good Night")
    speak("Hello Leela krishna.")
    speak("I am Alida. How may I help you?")



def takeCommand():
    #It take mic input from user and returns string output.

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print("User said:",query)

    except Exception:
        #print(e)
        print("Say that again please...")
        return "None"
    return query

def sendEmail(to,content):
    server = smtplib.SMTP('smtp.gamil.com',587)
    server.ehlo()
    server.starttls()
    server.login('trafdlaw4@gmail.com','asdfg12345@')
    server.sendmail('trafdlaw4@gmail.com',to,content)
    server.close

def shutdown():
    speak("Yes Leela, terminating all the processess")
    speak("going offline.Shutting down your computer, See you next time,Jai Shree Raam.")
    os.system("shutdown -s")


def sleep():
    speak("OK Leela, I am going to sleep")
    os.system("sleep -s")





if __name__ == "__main__":
    wishMe()
    #query1=takeCommand().lower()
    while 1 :
        #query1=takeCommand().lower()
        #if 'hey' in query1:
            speak("yes how may I help you")
            query = takeCommand().lower()
            #logic for executing tasks based on query
            if 'wikipedia' in query:
                speak('Searching wikipedia...')
                query = query.replace("wikipedia","")
                results = wikipedia.summary(query, sentences=2)
                speak("According to wikipedia")
                print(results)
                speak(results)
            elif 'wish me' in query:
                wishMe()
            elif 'open youtube' in query:                                     #youtube
                web.open("https://www.youtube.com/")
            elif 'open google' in query:                                      #google
                web.open("https://www.google.com/?gws_rd=ssl")
            elif 'play music' in query:                                       #music
                music_dir='C:\\Music\\songs'
                songs=os.listdir(music_dir)
                print(songs)
                os.startfile(os.path.join(music_dir,songs[0]))
            elif 'the time' in query:                                         #time
                nowtime=datetime.datetime.now().strftime("%H:%M:%S")
                speak(f"now the time is {nowtime}")
            elif 'email to leela' in query:                                   #mail 
                try:
                    speak("What shput I say")
                    content=takeCommand()
                    to="leelabrr27@gmail.com"
                    sendEmail(to,content)
                    speak("Mail has been sent")
                except Exception as e:
                    print(e)
                    speak("Sorry leela. Not able to send this mail at the moment")
            elif 'shutdown' in query:                                         #shutdown
                #shutdown()
            elif 'quit' in query:                                              #quit
                quit()
            elif 'sleep' in query:                                             #sleep
                #sleep()

    