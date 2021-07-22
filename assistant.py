import pyttsx3
import speech_recognition as sr
import webbrowser
import datetime
import wikipedia
import subprocess
import re





master="Jarvis"
assin="Stark"
def command():
    s=sr.Recognizer()
    
    
    
    with sr.Microphone() as mike:
        print("Listening")
        
        
        
        
        s.pause_threshold = 1
        audio = s.listen(mike)
        
        
        
        
        
        
        try:
            print("Recognizing Command")
            
            
            
            
            command = s.recognize_google(audio,language="en-in")
            print("Command: "+command)
            
        except Exception as e:
            print(e)
            return "None"
        
        return command
    
def speak(audio): 
    
    engine = pyttsx3.init() 
    
    
    voices = engine.getProperty('voices') 
    
    
    
    engine.setProperty('voice', voices[1].id) 
    engine. setProperty("rate", 175)
    
    engine.say(audio)   
    
    
    
    engine.runAndWait()
    
def tellDay(): 
      
    
    
    day = datetime.datetime.today().weekday()
          
    
    
    Day_dict = {0: 'Monday', 1: 'Tuesday',  
                2: 'Wednesday', 3: 'Thursday',  
                4: 'Friday', 5: 'Saturday', 
                6: 'Sunday'}
      
    if day in Day_dict.keys(): 
        day_of_the_week = Day_dict[day] 
        print(day_of_the_week) 
        speak("The day is " + day_of_the_week)
    
def tellTime(): 
      
    
    time = str(datetime.datetime.now())
    
    
    
    
    
    
    day = datetime.date(day=int(time[8:10]), month=int(time[5:7]), year=int(time[0:4])).strftime('%A %d %B %Y')
    speak("The time is " + time[11:13] + " " + time[14:16] + ". Today is " + day)
    
def Whatsapp(phone,text):
    try:
        subprocess.Popen(["cmd", "/C", "start whatsapp://send?phone=91"+str(phone)+"^&text="+text], shell=True)
    except Exception as e:
        pass

def Hello(): 
      
    
    
    
    try:
        time = str(datetime.datetime.now())
        hour = int(time[11:13])
        if hour < 12 and hour >= 2:
            phase = "Morning"
        elif hour >= 12 and hour < 16:
            phase = "Afternoon"
        else:
            phase = "Evening"

        speak("Good "+ phase + master +" sir I am your desktop assistant, "+ assin +". Tell me how may I help you!?")
    except Exception as e:
        pass
    
def assistant():
    
    while(True):
        comm=command().lower()
        if "time" in comm:
            tellTime()
        elif "in wikipedia" in comm or "on wikipedia" in comm or "from wikipedia" in comm:
            if "in wikipedia" in comm:
                comm.replace("in wikipedia","")
            elif "on wikipedia" in comm:
                comm.replace("on wikipedia","")
            else:
                comm.replace("from wikipedia","")
            res = wikipedia.summary(comm, sentences=3) 
            speak("According to wikipedia, ")
            print("According to Wikipedia,") 
            speak(res)
            print(res)
        elif "bye" in comm:
            speak("GoodBye! Will be waiting for you (wink)")
            break
        elif "whatsapp" in comm:
            try:
                mess = (re.search('whatsapp (.+?) to', comm).group(1)).replace(" ","%20")
                print(mess)
                s = re.findall(r'\d+', comm)
                num = "".join(s)
                Whatsapp(num,mess)
                break
            except AttributeError:
                
                print("Message not found") 
        elif comm!="none":
            webbrowser.open("http://google.com/?#q="+comm)
        print("Do you wish to continue?")
        if command().lower()=="yes":
            continue
        else:
            break
assistant()