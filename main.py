import pyttsx3  # Text-to-speech conversion library
import speech_recognition as sr  # Library for speech recognition
import datetime  # To handle date and time
import time  # Time-related functions
import webbrowser  # To open web pages
import pyautogui  # For GUI automation like pressing keys

def initialize_engine():
    """
    Initializes the text-to-speech engine with custom settings for voice, rate, and volume.
    """
    engine = pyttsx3.init("sapi5")  # Initializes the speech engine
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)  # Selects a female voice
    rate = engine.getProperty('rate')
    engine.setProperty('rate', rate-50)  # Slows down the speech rate
    volume = engine.getProperty('volume')
    engine.setProperty('volume', volume+0.25)  # Increases volume slightly
    return engine


def speak(text):
    """
    Converts the given text to speech.
    """
    engine = initialize_engine()
    engine.say(text)
    engine.runAndWait()





def command():
    """
    Listens to the user's voice command and converts it into text using Google's speech recognition API.
    """
    r = sr.Recognizer()  # Initialize the recognizer
    
    # Setting up the microphone for listening
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source, duration=0.5)  # Adjusts for ambient noise
        print("Listening...")
        r.pause_threshold = 1.0  # Time to wait before considering speech as ended
        r.phrase_threshold = 0.3  # Minimum length of a phrase for it to be recognized
        r.sample_rate = 48000  # Sample rate for audio
        r.dynamic_energy_threshold = True  # Enables dynamic energy threshold adjustment
        r.operation_timeout = 5  # Timeout for listening operation
        r.non_speaking_duration = 0.5  # Duration of silence to detect end of speech
        r.dynamic_energy_adjustment = 2  # Adjustment factor for dynamic energy threshold
        r.energy_threshold = 4000  # Energy level for detecting speech
        r.pause_time_limit = 10  # Max duration to pause before stopping
        print(sr.Microphone.list_microphone_names())  # List available microphones
        audio = r.listen(source)  # Listen for the audio input
        
    try:
        # Attempt to recognize speech
        print("\r", end="", flush=True)
        print("Recognizing...", end="", flush=True)
        query = r.recognize_google(audio, language='en-in')  # Use Google API for recognition
        print("\r", end="", flush=True)
        print(f"User said: {query}\n")
    except Exception as e:
        # Handle exceptions and request the user to repeat
        print("Say that again please...")
        return "None"
    return query




def cal_day():
    """
    Calculates and prints the current day of the week.
    """
    day = datetime.datetime.today().weekday() + 1  # Get the current day as a number (1-7)
    day_dict = {1: 'Monday', 2: 'Tuesday', 3: 'Wednesday', 4: 'Thursday',
                5: 'Friday', 6: 'Saturday', 7: 'Sunday'}  # Mapping of day numbers to names
    if day in day_dict.keys():
        day_of_the_week = day_dict[day]  # Get the corresponding day name
        print(day_of_the_week)  # Print the day
    return day_of_the_week




def wishMe():
    """
    Greets the user based on the current time of the day.
    """
    hour = int(datetime.datetime.now().hour)
    t = time.strftime("%I:%M %p")
    day = cal_day()
    if (hour>=0) and (hour<12) and ("AM" in t):
        speak(f"Good Morning! Rushabh, its {day} and the time is {t}")
    elif (hour>=12) and (hour<18) and ("PM" in t):
        speak(f"Good Afternoon! Rushabh, its {day} and the time is {t}")
    else:
        speak(f"Good Evening! Rushabh, its {day} and the time is {t}")




def Web(command):
    """
    Opens social media websites based on the command.
    """
    platforms = {
        # "facebook": "facebook.com",
        # # "whatsapp": "web.whatsapp.com",
        # "instagram": "instagram.com",
        # "youtube": "youtube.com"
        "Google": "https://www.google.com/",
        "LinkedIn": "https://www.linkedin.com/",
        "Github": "Github.com"
    }
    for key, url in platforms.items():
        if key in command:
            speak(f"Opening {key}")
            webbrowser.open(url)
            break




def schedule():
    """
    Opens the daily study schedule.
    """
    day = cal_day().lower()
    speak(f"Opening Rushabh's Silent Hustle for {day}")
    webbrowser.open("schedule.txt")




def openApp(command):
    """
    Opens common Windows applications based on the command.
    """
    apps = {
        "calculator": "calculator",
        "paint": "paint",
        "notepad": "notepad",
        "whatsapp": "whatsapp",
        "instagram": "instagram",
        "youtube": "youtube",
        "facebook": "facebook"
    }
    for key, app in apps.items():
        if key in command:
            speak(f"Opening {key}")
            pyautogui.press("win")
            pyautogui.write(app)
            pyautogui.press("enter")
            break


def closeApp(command):
    """
    Closes common Windows applications based on the command.
    """
    apps = {
        "calculator": "calculator",
        "paint": "paint",
        "notepad": "notepad",
        "whatsapp": "whatsapp",
        "instagram": "instagram",
        "youtube": "youtube",
        "facebook": "facebook"

    }
    for key, app in apps.items():
        if key in command:
            speak(f"Closing {key}")
            pyautogui.hotkey("alt", "f4")
            break


if __name__ == "__main__": 
    wishMe()  # Greet the user
    while True:
        query = command().lower()
        # query = input("Enter your command: ")
        if ("Google" in query) or ("linkedin" in query) or ("GitHub" in query) :
            Web(query)
        elif ("Daily study Schedule" in query) or ("study" in query) or ("schedule" in query):
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

        elif ("open calculator" in query) or ("open paint" in query) or ("open notepad" in query) or ("open whatsapp" in query) or ("open instagram" in query) or ("open youtube" in query) or ("open facebook" in query):
            openApp(query)
        elif ("close calculator" in query) or ("close paint" in query) or ("close notepad" in query) or ("close whatsapp" in query) or ("close instagram" in query) or ("close youtube" in query) or ("close facebook" in query):
            closeApp(query)
           




        # if "exit" in query:
        #     speak("Goodbye")
        #     break
        # else:
            # speak("I am listening...")  
        # print(query)
