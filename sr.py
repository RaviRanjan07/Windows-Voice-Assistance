import pyttsx3
import datetime
import speech_recognition as srd
import wikipedia
import smtplib
import webbrowser as wb
import psutil
import pyjokes
import os
import json
import requests
import random
import pyautogui
from urllib.request import urlopen
import wolframalpha
import time

engine=pyttsx3.init()
wolframalpha_app_id='UJLXJG-XYWKK2H7YX'
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def times():
    Time=datetime.datetime.now().strftime("%H:%M:%S")
    speak("The current time is")
    speak(Time)

def date():
    Date=datetime.datetime.now().day
    Month=datetime.datetime.now().month
    Year=datetime.datetime.now().year
    speak("the current date is")
    speak(Date)
    speak(Month)
    speak(Year)

def wishme():
    speak("welcome Buddy")
    times()
    date()
    hour=datetime.datetime.now().hour
    if(hour>=6 and hour<12):
        speak("Good Morning Sir")
    elif (hour >= 12 and hour < 18):
        speak("Good Afternoon Sir")
    elif (hour >= 18 and hour < 24):
        speak("Good Evening Sir")
    else:
        speak("Good Night")

    speak("SpiffyLine at your service. please tell me how can i help you today")

def TakeCommand():
    r=srd.Recognizer()
    with srd.Microphone() as source:
        print("Listening....")
        r.pause_threshold=1
        audio=r.listen(source)
    try:
        print("Recognizing...")
        query=r.recognize_google(audio,language='en-in')
        print(query)
    except Exception as e:
        print(e)
        print("Say that again please")
        return "None"
    return query

def sendEmail(to,content):
    server=smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('nikhilboricha777@gmail.com','Nikhil@99')
    server.sendmail('nikhilboricha777@gmail.com',to,content)
    server.close()

def cpu():
    usage=str(psutil.cpu_percent())
    speak("cpu is at"+usage)
    battery=psutil.sensors_battery()
    speak("Battery is at")
    speak(battery.percent)

def joke():
    speak(pyjokes.get_joke())

def screenshot():
    img=pyautogui.screenshot()
    img.save('D:/screenshot.png')

if __name__ == "__main__":
    wishme()

    while True:
        query= TakeCommand().lower()

        if 'time' in query:
            times()

        elif 'date' in query:
            date()

        elif 'wikipedia' in query:
            speak('searching.....')
            query=query.replace('wikipedia','')
            result=wikipedia.summary(query,sentences=3)
            speak('According to wikipedia')
            print(result)
            speak(result)

        elif 'send email' in query:
            try:
                speak("What should i say?")
                content=TakeCommand()
                speak("who is the receiver")
                receiver=input("Enter Receiver email")
                to=receiver
                sendEmail(to,content)
                speak(content)
                speak("Email is send succesfully")
            except Exception as e:
                print(e)
                speak("Unable to send mail")

        elif 'search in chrome' in query:
            speak("please tell about search")
            chromepath="C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s"
            search=TakeCommand().lower()
            wb.get(chromepath).open_new_tab(search+'.com') #this is only useful for the .com website
        
        elif 'search youtube' in query:
            speak("what should I search")
            search_term=TakeCommand().lower()
            speak("Here we go to youtube")
            wb.open('https://www.youtube.com/results?search_query='+search_term)
        
        elif 'search google' in query:
            speak("what should I search")
            search_term=TakeCommand().lower()
            speak("Searching")
            wb.open('https://www.google.com/search?q='+search_term)

        elif 'cpu' in query:
            cpu()
        
        elif 'what is your name' in query:
            speak("My name is Spiffy line iam a digital assistant")
            speak("pls tell your name")
            ty=TakeCommand().lower()
            speak("Now i am remember your Name is"+ty)

        
        elif 'joke' in query:
            joke()

        elif 'go offline' in query:
            speak("Going Offline sir")
            quit()

        elif 'word' in query:
            speak("Opening Ms Word......")
            ms_word='C:/ProgramData/Microsoft/Windows/Start Menu/Programs/Microsoft Office 2013/Word 2013'
            os.startfile(ms_word)

        elif 'write a note' in query:
            speak("what shoould i write,sir")
            notes = TakeCommand()
            file=open('notes.txt','w')
            speak("Sir should i include date and time")
            ans=TakeCommand()
            if 'yes' in ans or 'sure' in ans:
                strTime=datetime.datetime.now().strftime("%H:%M:%S")   
                file.write(strTime)
                file.write(':-')
                file.write(notes)
                speak("Done Taking Notes, Sir")
            else:
                file.write(notes)

        elif 'note' in query:
            speak("showing notes")
            file=open('notes.txt','r')
            print(file.read())
            speak(file.read())

        elif 'screenshot' in query:
            screenshot()
        
        elif 'remember that' in query:
            speak("What should i remember?")
            memory=TakeCommand()
            speak("You asked me to remember that"+memory)
            remember=open('memory.txt','w')
            remember.write(memory)
            remember.close()

        elif 'remember anything' in query:
            remember=open('memory.txt','r')
            speak("You asked me to remember that"+remember.read())

        elif 'news' in query:
            try:
                jsonobj=urlopen('http://newsapi.org/v2/top-headlines?country=us&category=entertainment&apiKey=069a6ba2278844909e5be02ef3521399')
                data=json.load(jsonobj)
                i=1
                speak("Here are some top headlines from the Entertainment Industry")
                print("==========Top HEadlines===========")
                for item in data['articles']:
                    print(str(i)+'. '+item['title']+'\n') 
                    print(item['description']+'\n')
                    speak(item['title'])
                    i=i+1

            except Exception as e:
                print(str(e))   

        elif 'where is' in query:
            query=query.replace('where is',"")
            location=query
            speak("User asked to locate"+location)
            wb.open_new_tab("https://www.google.com/maps/place/"+location)

        elif 'stop listening' in query:
            speak('For how many seconds you want me to stop listening to your command?')
            ans=int(TakeCommand())
            time.sleep(ans)
            print(ans)
        
        elif 'log out' in query:
            os.system("shutdown -l")
        elif 'restart' in query:
            os.system("shutdown /r /t 1")
        
        elif 'calculate' in query:
            client=wolframalpha.Client(wolframalpha_app_id)
            indx=query.lower().split().index('calculate')
            query=query.split()[indx + 1:]
            res=client.query(''.join(query))
            answer=next(res.results).text
            print('the answer is :'+answer)
            speak('the answer is :'+answer)
        
        elif 'what is' in query or 'who is' in query:
            client=wolframalpha.Client(wolframalpha_app_id)
            res=client.query(query)

            try:
                print(next(res.results).text)
                speak(next(res.results).text)
            except StopIteration:
                print("No Results")