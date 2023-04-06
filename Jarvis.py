import pyttsx3
import datetime
import speech_recognition as sr
import webbrowser
import subprocess
import wikipedia
import os
import random

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)

rate = engine.getProperty('rate')
engine.setProperty('rate', 200)

volume = engine.getProperty('volume')
engine.setProperty('volume',1)

def speaking(tell):
    '''
    This function will speak everytime its called with a given string argument
    :param tell:
    :return:
    '''
    engine.say(tell)
    engine.runAndWait()

def Wish():
    '''
    This function will  wish me according to time
    :return:
    '''
    hour=(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speaking("Good Morning")
    elif hour>=12 and hour<16:
        speaking("Good afternoon")
    else:
        speaking("Good evening")
    speaking("How may I help you")
def takeSpeech():
    '''
    This function will take an audio input and return the statement
    :return:
    '''
    
    r= sr.Recognizer()
    print("Listening....")
    r.pause_threshold=0.6
    r.phrase_threshold=0.5
    r.energy_threshold=400
    with sr.Microphone() as source:
        audio = r.listen(source)
    print("rt")

    try:
        print("Recoganizing..")
        said = r.recognize_google(audio, language='en-in')
        print(f"You meant- {said}")

    except Exception as e:
        print(f"Couldn't understand {str(e)}")
        print("Please say again")
        return "none"

    return said

if __name__ == '__main__':

    Wish()

    # while True:
    if 1:
        
        convert = takeSpeech().lower()
        print(convert)

        #now building logics for doing several things

        if 'open youtube' in convert:
            webbrowser.open("youtube.com")
        elif 'open google' in convert:
            webbrowser.open("google.com")
        elif 'wikipedia' in convert:
            speaking("Searching wikipidea")
            convert=convert.replace("wikipidea","")
            result = wikipedia.summary(convert, sentences=2)
            speaking("Acording to wikipidea")
            print(result)
            speaking(result)
        elif 'open notepad' or 'write some notes' in convert:
            speaking('opening notepad')
            os.system('notepad')
        elif 'open pictures' or 'show pictures' in convert:
            pics_dir = 'E:\\pics'
            pics = os.listdir(pics_dir)
            print(pics)
            os.startfile(os.path.join(pics_dir, random.choice(pics)))
        elif 'the time' in convert:
            ntime= datetime.datetime.now().strftime("%H:%M:%S")
            speaking(f"The time is {ntime}")
