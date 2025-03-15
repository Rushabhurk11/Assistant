import pyttsx3 #!pip install pyttsx3
import speech_recognition as sr
import datetime
import time
import webbrowser
import pyautogui #!pip install pyautogui

def initialize_engine():
    engine = pyttsx3.init("sapi5")
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)
    rate = engine.getProperty('rate')
    engine.setProperty('rate', rate-50)
    volume = engine.getProperty('volume')
    engine.setProperty('volume', volume+0.25)
    return engine

def speak(text):
    engine = initialize_engine()
    engine.say(text)
    engine.runAndWait()

def command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source, duration=0.5)
        print("Listening...")
        r.pause_threshold = 1.0
        r.phrase_threshold = 0.3
        r.sample_rate = 48000
        r.dynamic_energy_threshold = True
        r.operation_timeout = 5
        r.non_speaking_duration = 0.5
        r.dynamic_energy_adjustment=2
        r.energy_threshold = 4000
        r.pause_time_limit = 10
        print(sr.Microphone.list_microphone_names()) 
        audio = r.listen(source)
        
    try:
        print("\r" , end="", flush=True)
        print("Recognizing...", end="", flush=True)
        query = r.recognize_google(audio, language='en-in')
        print("\r" , end="", flush=True)
        print(f"User said: {query}\n")
    except Exception as e:
        print("Say that again please...")
        return "None"
    return query



def cal_day():
    day = datetime.datetime.today().weekday() + 1
    day_dict = {1: 'Monday', 2: 'Tuesday', 3: 'Wednesday', 4: 'Thursday', 5: 'Friday', 6: 'Saturday', 7: 'Sunday'}
    if day in day_dict.keys():
        day_of_the_week = day_dict[day]
        print(day_of_the_week)
    return day_of_the_week



def wishMe():
    hour = int(datetime.datetime.now().hour)
    t = time.strftime("%I:%M:%p")
    day = cal_day()
    if (hour>=0) and (hour<12) and ("AM" in t):
        speak(f"Good Morning! Rushabh, it's {day} and the time is {t}")
    elif (hour>=12) and (hour<18) and ("PM" in t):
        speak(f"Good Afternoon! Rushabh, it's {day} and the time is {t}")
    else:
        speak(f"Good Evening! Rushabh, it's {day} and the time is {t}")

    # speak("I am your edit. Please tell me how may I help you") 



def social_media(command):
    if "facebook" in command:
        speak("Opening Facebook")
        webbrowser.open("facebook.com")
    elif "whatsapp" in command:
        speak("Opening Whatsapp")
        webbrowser.open("web.whatsapp.com")
    elif "instagram" in command:
        speak("Opening Instagram")
        webbrowser.open("instagram.com")
    elif "youtube" in command:
        speak("Opening Youtube")
        webbrowser.open("youtube.com")



def schedule():
    day = cal_day().lower()
    speak(f"Opening the schedule for {day}")
    webbrowser.open("schedule.txt")

def openApp(command):
    if "calculator" in command:
        speak("Opening Calculator")
        pyautogui.press("win")
        pyautogui.write("calculator")
        pyautogui.press("enter")
    elif "paint" in command:
        speak("Opening Paint")
        pyautogui.press("win")
        pyautogui.write("paint")
        pyautogui.press("enter")
    elif "notepad" in command:
        speak("Opening Notepad")
        pyautogui.press("win")
        pyautogui.write("notepad")
        pyautogui.press("enter")
    # elif "setting" in command:
    #     speak("Opening Setting")
    #     pyautogui.press("win")
    #     pyautogui.write("settings")
    #     pyautogui.press("enter") 





if __name__ == "__main__": 

    #----------------- Uncomment the below line for wishing the user
    wishMe() 
    while True:
       
        
        # query = command().lower()
        query = input("Enter your command: ")
        if ("facebook" in query) or ("whatsapp" in query) or ("instagram" in query) or ("youtube" in query):
            social_media(query)
        elif ("Daily study Schedule" in query) or ("study" in query):
            schedule()
        elif ("volume up" in query) or ("increase volume" in query):
            pyautogui.press("volumeup")
            speak("Volume increased")
        elif ("volume down" in query) or ("decrease volume" in query):
            pyautogui.press("volumedown")
            speak("Volume decreased")
        elif ("volume mute" in query) or ("mute the sound" in query):
            pyautogui.press("volumemute")
            speak("Volume muted")
        elif ("play" in query):
            pyautogui.press("playpause")

        elif ("open calculator" in query) or ("open paint" in query) or ("open notepad" in query) #or ("open setting" in query):
            openApp(query)
           



        if "exit" in query:
            speak("Goodbye")
            break
        # else:
            # speak("I am listening...")  
        # print(query)


# speak("Hello, I am your edit. How can I help you?")
