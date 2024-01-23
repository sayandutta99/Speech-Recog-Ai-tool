from ast import While
import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def talk(text):
    engine.say(text)
    engine.runAndWait()


def take_command():
    try:
        with sr.Microphone() as source:
            print('listening')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            # command = command.lower()
            # if 'SayanBot' in command:
            # command=command.replace('SayanBot','')
            print(command)



    except:
        pass
    return command


def run_alexa():
    command = take_command()
    print(command)
    if 'play' in command:
        song = command.replace('play', '')
        talk('playing' + song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%H:%M')  
        print   (time)
        talk('Current time is'+ time)
        
    elif 'who is' in command:
        person = command.replace ('who is','')
        info= wikipedia.summary(person,10)
        print (info)
        talk(info)
    elif 'date' in command:
        talk('Sorry, I have a Boyfriend')
    elif 'will you marry me' in command:
        talk('Sorry babe I have a boyfriend')
        
    elif 'joke' in command:
        talk(pyjokes.get_joke())
        
    else:
        talk('Please say the command again.')

run_alexa()
        

