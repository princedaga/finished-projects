import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices[0].id) 
engine.setProperty('voice', voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def Wishme():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning sir!")

    elif hour >= 12 and hour < 18:
        speak("Good Afternoon sir!")

    else:
        speak("Good Evening sir!")

    speak("Hello sir! I am electra. Tell me how may I help you.")

def takecommand():
    #it takes microphone input from user...

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

        try:
            print("Recognizing...")
            speak("Recognizing...")
            query = r.recognize_google(audio, language='en-IN')
            print(f"User said: {query}\n")
        except Exception as e:
            #print(e)

            print("Say that again please... ")
            speak("Say that again please... ")
            return "None"
        return query
def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail,com', 587)
    server.ehlo()
    server.starttls()
    server.login('manasvijaju809@gmail.com', 'Missmee76_')
    server.sendmail('manasvijaju809@gmail.com', to, content)
    server.close()

if __name__ == "__main__":
    Wishme()
    while True:
        query = takecommand().lower()

        #logic...
        if 'wikipedia' in query:
            speak('searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=10)
            speak("according to wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")  

        elif 'open google' in query:
            webbrowser.open("google.com")  

        elif 'open instagram' in query:
            webbrowser.open("instagram.com")

        elif 'open my site' in query:
            webbrowser.open("googlepvt.netlify.app")

        elif 'play music' in query:
           music_dir = ''
           songs = os.listdir(music_dir)
           print(songs)
           os.startfile(os.path.join(music_dir, songs[0]))

        elif 'time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"sir, the time now is {strTime}")

        elif 'open code' in query:
            codepath = "C:\\Users\\princ\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codepath)

        elif 'email to prince' in query:
            try:
                speak("what should i say?")
                content = takecommand()
                to = "princejain0479@gmail.com"
                sendEmail(to, content)
                speak("email has been sent!")
            except Exception as e:
                print(e)
                speak("sorry sir. i am not able to send this email")

        if SystemExit:
            speak("Exit Successfull")
            break