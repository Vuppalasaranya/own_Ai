import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia as wiki 
import pyautogui as pag
import pyscreeze
import json
import requests
import openai 
import pywhatkit as pw
import smtplib as ml
import sample
import os
x=pyttsx3.init()
headers = {"Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjoiNjA4ZDNkZWMtNTkzNC00Y2I3LWFmMGUtMmUwNmEyODVmODhjIiwidHlwZSI6ImFwaV90b2tlbiJ9.g_U0ET9GqEREJJ7GyvF38qgYV0R9Ijt7qs0tzvevdFU"}

url = "https://api.edenai.run/v2/text/chat"
payload = {
    "providers": "openai",
    "text": "Hello i need your help ! ",
    "chatbot_global_action": "Act as an assistant",
    "previous_history": [],
    "temperature": 0.0,
    "max_tokens": 150,
    "fallback_providers": "abcd"
}

def talktoai(query):
    payload["text"]=query
    response = requests.post(url, json=payload, headers=headers)
    result = json.loads(response.text)
    speak(result['openai']['generated_text'])

def speak(audio):
    x.say(audio)
    x.runAndWait()
# speak("Hi I am Itachi AI How can i help you")
def time():
    t=datetime.datetime.now().strftime("%H:%M:%S")
    # print(t)
    speak(t)
# time()
def date():
    y=str(datetime.datetime.now().year)
    m=str(datetime.datetime.now().month)
    d=str(datetime.datetime.now().day)
    speak(d)
    speak(m)
    speak(y)
    # print(y)
# date()
def youtube(ele):
    pw.playonyt(ele)
def chrome(ele):
    pw.search(ele)
def whatsapp(t,msg):
    pw.sendwhatmsg_instantly(t,msg)
def sendmail(to,msg):
    server=ml.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login('vuppalasaranya@gmail.com','kpwv tqdb funu jwiw')
    server.sendmail('vuppalasaranya@gmail.com',to,msg)
    server.close()
def wish():
    h = datetime.datetime.now().hour
    if h<12:
        speak("Good Morning ")
    elif h>=12 and h<=18:
        speak("Good Afternoon ")
    elif h>18 and h<=21:
        speak("Good Evening")
    else:
        speak("Good Night ")
    # speak("Hello Srinivas")
    speak("How can i help you today")
# str=input()
# wish()
def inp():
    x1 = sr.Recognizer()
    with sr.Microphone() as                                                                                                          source:
        print("listening...")
        x1.pause_threshold=1
        audio=x1.listen(source)
        try:
            print("Recognizing...")
            query = x1.recognize_google(audio,language='en-in')
            print(query)
        except Exception as e:
            print(e)
            speak("Can you repeat again")
            inp()
            return "None"
        return query
def screenshot():
    im1=pyscreeze.screenshot()
    im2=pyscreeze.screenshot('myim.png')
# inp()
if __name__ =="__main__":
    wish()
    while True:
        query=inp().lower()
        if "time" in query:
            time()
        elif "date" in query:
            date()
        elif "wikipedia" in query:
            print("I'm searching...")
            query=query.replace("wikipedia","")
            search=wiki.summary(query,sentences=5)
            print(search)
            speak(search)
        elif "screenshot" in query:
            speak("I'm taking screenshot...")
            screenshot()
        elif "exit" in query:
            speak("Exiting")
            # print("bye bye")
            exit()
        elif "email" in query:
            try:
                speak("What message do you want to send")
                msg=input()
                speak("Please enter recipients email")
                to=input()
                sendmail(to,msg)
                speak("Mail sent successfully")
            except Exception as e:
                print(e)
                speak("failed to send")
        elif "youtube" in query:
            speak("What do you want me to search")
            ele=inp()
            speak("Opening youtube")
            youtube(ele)
            exit()
        elif "whatsapp" in query:
            try:
                speak("Enter the number")
                t=input()
                speak("Tell me the message to send")
                msg=inp()
                whatsapp(t,msg)
            except Exception as e:
                print(e)
                speak("Failed to send")
        elif "search" in query:
            speak("What do you want me to search")
            ele=inp()
            speak("Opening Chrome")
            chrome(ele)
        elif "remember" in query:
            speak("Tell me what to remember")
            rem=inp()
            speak("You asked me to remember"+rem)
            remember=open('rem.txt','w')
            remember.write(rem)
            remember.close()
        elif "to save" in query:
            remember=open('rem.txt','r')
            speak("You told me to store"+remember.read())
        elif "play song" in query:
            song_path=input("Enter the song path:")
            sample.play_song(song_path)
        elif "pause the song" in query:
            sample.control("pause")
        elif "unpause" in query:
            sample.control("unpause")
        elif "play" in query:
            try:
                sample.play_song(song_path)
            except:
                print("please say play a song")
        elif "stop" in query:
            sample.control("stop")
        elif "shutdown my pc" in query:    
            os.system("shutdown /s /t 1")
        elif "restart my pc" in query:
            os.system("shutdown /r /t 1") 
        else:
            talktoai(query)