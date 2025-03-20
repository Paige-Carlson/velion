import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser
import random
import time

# Initialize speech engine
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)  # Female voice

def speak(text):
    print(f"Assistant: {text}")
    engine.say(text)
    engine.runAndWait()

def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)
        
        try:
            text = r.recognize_google(audio).lower()
            print(f"You: {text}")
            return text
        except sr.UnknownValueError:
            return ""
        except sr.RequestError:
            speak("Sorry, I'm having trouble connecting to the internet")
            return ""

def greet():
    hour = datetime.datetime.now().hour
    if 5 <= hour < 12:
        speak("Good morning! How can I help you?")
    elif 12 <= hour < 18:
        speak("Good afternoon! How can I assist?")
    else:
        speak("Good evening! What can I do for you?")

def get_time():
    current_time = datetime.datetime.now().strftime("%I:%M %p")
    speak(f"The current time is {current_time}")

def play_music():
    speak("Playing some relaxing music")
    webbrowser.open("https://www.youtube.com/watch?v=4xDzrJKXOOY")

def set_timer(seconds):
    speak(f"Timer set for {seconds} seconds")
    time.sleep(seconds)
    speak("Time's up! Your timer has ended")

def get_joke():
    jokes = [
        "Why don't scientists trust atoms? Because they make up everything!",
        "What do you call fake spaghetti? An impasta!",
        "Why did the scarecrow win an award? Because he was outstanding in his field!"
    ]
    speak(random.choice(jokes))

def search_web(query):
    speak(f"Searching for {query}")
    webbrowser.open(f"https://www.google.com/search?q={query}")

def handle_command(command):
    if "time" in command:
        get_time()
    elif "play music" in command:
        play_music()
    elif "timer" in command:
        try:
            minutes = int(''.join(filter(str.isdigit, command)))
            set_timer(minutes * 60)
        except:
            speak("Please specify a valid time")
    elif "joke" in command:
        get_joke()
    elif "search" in command:
        query = command.replace("search", "").strip()
        search_web(query)
    elif "exit" in command or "quit" in command:
        speak("Goodbye!")
        exit()
    else:
        speak("I didn't understand that command")

if __name__ == "__main__":
    greet()
    while True:
        command = listen()
        if command:
            handle_command(command)
        else:
            speak("Could you please repeat that?")
