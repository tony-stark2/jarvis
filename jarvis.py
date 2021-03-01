import pyttsx3 #pip install pyttsx3
import speech_recognition as sr #pip install speechRecognition
import datetime
import wikipedia #pip install wikipedia
import webbrowser #pip install webbrowser
import os
import cv2
import time
import random
import pyjokes #pip install Pyjokes
from requests import get #pip install requests
import sys
import pywhatkit as kit
import smtplib
import pyautogui #pip install PyAutoGUi



engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    tt = time.strftime("%I:%M %p")

    if hour>=0 and hour<12:
        speak(f"Good Morning Boss, its {tt}")

    elif hour>=12 and hour<18:
        speak(f"Good Afternoon Boss, its {tt}")   

    else:
        speak(f"Good Evening Boss, its {tt}")  

    speak("I'm jarvis . your personal assistant, how may i help you")       

def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source,timeout=1,phrase_time_limit=5)
    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)    
        speak(" sorry boss, Say that again please...")  
        return "None"
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('your email', 'password')
    server.sendmail('your email', to, content)
    server.close()
    
def news():
    main_url = "newapi key"

    main_page = requests.get(main_url).json()
    #print(main_page)
    articles = main_page["articles"]
    #print(articles)
    head=[]
    day=["first","second","third","fourth","fifth"]
    for ar in articles:
        head.append(ar["title"])
    for i in range(len(day)):
        #print(f"today's {day[i]} news is:", head[i])
        speak(f"today's {day[i]} news is:", head[i])


if __name__ == "__main__":
    wishMe()
    while True:
    # if 1:
        query = takeCommand().lower()

        # Logic for executing tasks based on query
        if 'wikipedia' in query:
            try:
                speak('Searching Wikipedia...')
                query = query.replace("wikipedia", "")
                results = wikipedia.summary(query, sentences=10)
                speak("Boss, According to Wikipedia")
                #print(results)
                speak(results)
            except Exception as e:
                speak("sorry boss, i can't find it") 

        elif "open notepad" in query:
            npath = "C:\\WINDOWS\\system32\\notepad.exe"
            speak("opening notepad Boss")
            os.startfile(npath) 
        
        elif "open command prompt" in query:
            speak("opening command prompt Boss")
            os.startfile("start cmd")

        elif "close command prompt" in query:
            speak("closing command prompt")
            os.system("taskkill /f /im Command Prompt.exe")

 
        elif "set alarm at 4 p.m." in query:
            nn = int(datetime.datetime.now().hour)
            if nn==16:
                music_dir = 'E:\\asad\\Music\\kgf original ringtone'
                songs = os.listdir(music_dir)
                os.startfile(os.path.join(music_dir, songs[1]))
            speak("your alarm has been set for 4:00 pm boss")


        elif "camera" in query:
            speak("opening camera Boss")
            cap = cv2.VideoCapture(0)
            while True:
                ret,img=cap.read()
                cv2.imshow('webcam',img)
                k = cv2.waitKey(50)
                if k==27:
                    break;

        elif "joke" in query:
            joke = pyjokes.get_joke()
            speak(joke)

        elif "change the window" in query:
            pyautogui.KeyDown("alt")
            pyautogui.press("tab")
            time.sleep(1)
            pyautogui.KeyUp("alt")

        elif "news" in query:
            speak("please give me some time to find out the latest news boss")
            news()

        elif "ip address" in query:
            ip = get('https://api.ipify.org').text
            speak(f"boss, your ip address is {ip}")

        elif "close notepad" in query:
            speak("closing notepad boss")
            os.system("taskkill /f /im notepad.exe")


        elif 'open youtube' in query:
            speak("opening youtube Boss")
            webbrowser.open("www.youtube.com")

        elif 'open google' in query:
            speak("opening google Boss")
            webbrowser.open("www.google.com")

        elif 'open stackoverflow' in query:
            speak("opening  Boss")
            webbrowser.open("www.stackoverflow.com")   


        elif 'time' in query:
            strTime = datetime.datetime.now().strftime("%I:%M %p")    
            speak(f"Boss, the time is {strTime}")


        elif "lms" in query:
            speak("opening your lms Boss")
            webbrowser.open("https://lms.simplilearn.com/dashboard")

        elif "thank you" in query:
            speak("most welcome, anytime boss")

        elif "it's not me" in query:
            speak("who the hell is using me, boss, don't give me to others. please")

        elif "who are you" in query:
            speak("I'm jarvis, syed asad's personal assistant, nice to meet you")

        elif "i asked who are you" in query:
            speak("are your deaf, i said that already that i'm jarvis syed asad's personal assistant, please don't ask silly questions to me")

        elif "open fast" in query:
            speak("be patient, i'm not playing game here.")

        elif "search" in query:
            speak("boss, what should i search?")
            cm = takecommand().lower()
            webbrowser.open(f"{cm}")

        elif "r studio" in query:
            npath = "D:\\Program Files\\RStudio\\bin\\rstudio"
            speak("opening R studio Boss")
            os.startfile(npath)   

        elif "send message to my dad" in query:
            speak("sending message to your dad boss")
            kit.sendwhatmsg("+919000532785","i send this message via my AI",19,55)    

        elif "play faded" in query:
            speak("playing boss")
            kit.playonyt("faded")

        elif "play music" in query:
            music_dir = "E:\\asad\\Music"
            songs = os.listdir(music_dir)
            rd = random.choice(songs)
            os.startfile(os.path.join(music_dir, songs[1]))

        elif "shut up" in query:
            speak("you shutup")

        elif "idiot" in query:
            speak("i'm not idiot, i'm a machine, if anyone is idiot among us, it is you. so don't mess with me")

        elif "say it again" in query:
            speak("golden words are not repeated. search it by yourself")

        elif "where do you live" in query:
            speak("in your imagination")

        elif "tell me about yourself" in query:
            speak("my name is jarvis, i'm  syed asad's personal assistant, nice to meet you, i will do what ever you want me to do. but only in this pc.")

        elif "why are you so lazy" in query:
            speak("Apne kaamse kam rakho. boss, don't give me to others, please")

        elif "breakfast" in query:
            speak("no boss, i do not eat anything, you know that right? did you had your breakfast boss")
            
        elif "yes thanks for asking" in query:
            speak("anytime boss, my work is to take care of you.")
                 
                
        elif "i am your dad" in query:
            speak("ohh, hello dad, i'm jarvis, how are you doing?")

        elif "i am your boss" in query:
            speak("are you sure about that? i don't think so, make it sure first. then talk to me")

        elif "good morning" in query:
            speak("good morning, how are you feeling today. did you had yourt breakfast?")

        elif 'email to dad' in query:
            try:
                speak("What should I say Boss?")
                content = takeCommand()
                to = "email of those whome you want to send email"    
                sendEmail(to, content)
                speak("Email has been sent Boss!")
            except Exception as e:
                print(e)
                speak("Sorry Boss,  I'm not able to send this email")    

        elif "close yourself" in query:
            speak("closing boss, have a nice day")
            sys.exit()

        elif "lunch" in query:
            speak("no, i don't eat anything boss")

        elif "how are you" in query:
            speak("i'm fine boss, what about you?")

        elif "battery" in query or "how much power is left" in query:
            import psutil
            battery = psutil.sensors_battery()
            percentage = battery.percent
            speak(f"boss our laptop have {percentage} percent battery left")

        elif "good night" in query:
            speak("good night boss, sleep well, sweet dreams boss")
            sys.exit()

        else:
            speak("sorry boss, you didn't program me for that")
