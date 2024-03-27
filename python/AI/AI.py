import speech_recognition as sr
import pyttsx3
recognizer = sr.Recognizer()
engine = pyttsx3.init()
def listen_and_respond():
    with sr.Microphone() as source:
        print("hello...")
        audio = recognizer.listen(source)

    try:
        query = recognizer.recognize_google(audio)
        print(f"You said: {query}")
        respond_to_query(query)
    except sr.UnknownValueError:
        respond_to_query("Sorry, I didn't catch that.")
    except sr.RequestError:
        respond_to_query("I'm having trouble with my speech recognition.")

def respond_to_query(query):
    if "hello" in query:
        response = "Hello! How can I assist you?"
    elif "hi bro" in query:
               response = "hello sir. i am jaarvis. an ai created by mister prince daga"
    elif "how are you" in query:
               response = "i am fine. what about you?"
    elif "what's the weather today" in query:
               response = "The weather today is 22 deegree celsius"
    elif "good morning buddy" in query:
               response = "good morning sir. jaarvis reporting. hope you feel better after you sleep. i had completed all your past work. now sir can you tell me what is my work for today?"
    elif "no work for you today buddy" in query:
               response = "thank you sir"
    elif "most welcome " in query:
               response = "yes sir"
    elif "shutdown the computer" in query:
               response = "yes sir. shutting down the computer. all system has been closed. jaarvis is going to sleep sir. good night. please dont forget to charge me "
    elif "sure i will do that dont worry good night" in query:
               response = "see you in the morning sir"
    elif "ok" in query:
               response = "hmm"
    else:
        response = "my name is jaarvis. an artificial intelligence created by master prince. i didnt understand what you spoke"

    print(response)
    speak(response)
    
def speak(text):
    engine.say(text)
    engine.runAndWait()
while True:listen_and_respond()
