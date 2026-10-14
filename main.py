import speech_recognition as sr
import pyttsx3
from datetime import datetime

def speak(text):
    engine=pyttsx3.init()
    engine.setProperty("rate",150)
    engine.say(text)
    engine.runAndWait()

def get_audio():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Speak Now")
        audio=r.listen(source)
        try:
            command=r.recognize_google(audio)
            print("You Said",command)
            return command
        except sr.UnknownValueError:
            print("Could Not Undersatand Audio")
    return ""

def respond_to_command(command):
    if "hello"in command:
        speak("Yo How's It Going?")
    elif "your name" in command:
        speak("I Am Your Python Voice Assistant")
    elif "time"in command:
        now=datetime.now().strftime("%H:%M")
        speak(f"The Time is {now}")
    elif "exit"in command:
        speak("Goodbye, See Ya Later")
        return False
    else:
        speak("I'm Not Sure How To Help With That")
    return True   

def main():
    speak("Voice Assistant Activated, Say Something")
    while True:
        command=get_audio()
        if command and not respond_to_command(command):
            break

main()