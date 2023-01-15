import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import time
import os
import smtplib
import random
import requests

import offline as os_ops
import online

USER_NAME = os.getenv('USER')
BOT_NAME = os.getenv('BOT_NAME')
num=random.randint(1,300)

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[0].id)
engine.setProperty('voices',voices[0].id)


def speak(audio):
     engine.say(audio)
     engine.runAndWait()


def wishMe():
    hour= int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")
    elif hour>=12 and hour<18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")

    speak("I am jarvis Sir. Please tell me how may I help you")


def echoMode():    # speak what he listens
    speak("Echo Mode On!")
    query = takeCommand()
    while not "echo mode off" in query:
        speak(query)
        query = takeCommand()

    speak("Echo Mode Off!")
    return


def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in') 
        print(f"User said: {query}\n") 

    except Exception as e:
        # print(e)    
        print("Say that again please...")   
        return "None" 
    return query

def sendEmail(to,content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('youremail@gmail.com', 'your-password')
    server.sendmail('youremail@gmail.com', to, content)
    server.close()


if __name__ =="__main__":
    wishMe()
    # while True:
    if 1:
        query=takeCommand().lower()

        if f"{BOT_NAME}" in query:
            query = query.replace(f"{BOT_NAME}", "")

        
        if 'wikipedia' in query:
            speak('searching wikipedia...')
            query= query.replace("wikipedia","")
            results = wikipedia.summary(query,sentences=1)
            speak("According to wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            speak('What do you want to play on Youtube, sir?')
            data = takeCommand().lower()
            online.play_on_youtube(data)

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open stack overflow' in query:
            webbrowser.open("stackoverflow.com")

        elif "search on google" in query:
            speak("what do you want to search on Google, Sir?")
            query = takeCommand().lower()
            online.search_on_google(query)

        elif "send whatsapp message" in query:
            speak('On what number should I send the message sir? Please enter in the console: ')
            number = input("Enter the number: ")
            speak("What is the message sir?")
            message = takeCommand().lower()
            online.whatsapp_message(number, message)
            speak("I've sent the message sir.")

        elif "news" in query:
            speak(f"I'm reading out the latest news headlines, sir")
            speak(online.get_latest_news())
            speak("For your convenience, I am printing it on the screen sir.")
            print(*online.get_latest_news(), sep='\n')

        elif 'weather' in query:
            ip_address = online.find_my_ip()
            city = requests.get(f"https://ipapi.co/{ip_address}/city/").text
            speak(f"Getting weather report for your city {city}")
            weather, temperature, feels_like = online.get_weather_report(city)
            speak(f"The current temperature is {temperature}, but it feels like {feels_like}")
            speak(f"Also, the weather report talks about {weather}")

        elif "advice" in query:
            speak("Here's an advice for you, sir")
            advice = online.get_random_advice()
            speak(advice)
            time.sleep(1)
            speak("For convenience, I am printing it on console")
            print(advice)

        elif "joke" in query:
            speak("Hope you like this one sir")
            joke = online.get_random_joke()
            speak(joke)
            print(joke)


        elif "open camera" in query:
            os_ops.open_camera()


        elif "open command prompt" in query or "open cmd" in query :
            os_ops.open_cmd()


        elif 'play music' in query:
            music_dir = 'C:\\Users\\aryan\\Music\\Music'
            songs = os.listdir(music_dir)
            # print(songs)    
            os.startfile(os.path.join(music_dir, songs[num]))


        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")


        elif 'open code' in query:
            codePath = "C:\\Users\\aryan\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Visual Studio Code"
            os.startfile(codePath)

        
        elif "screenshot" in query:
            if os_ops.takeScreenShot():
                speak("Screenshot saved in image folder")
            else:
                speak("Sorry! printing the error on consol")  


        elif os_ops.open_path(query.replace("open ", "")):
            pass


        elif 'email to aryan' in query:
            try:
                speak("What should i say?")
                content= takeCommand()
                to= "aryanguptaji184@gmail.com"
                sendEmail(to, content)
            except Exception as e:
                print(e)
                speak("Sorry. I am not able to send this email") 

        elif 'quit' in query:       
            exit()

    