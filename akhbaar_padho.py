import json

import requests
import json
def speak(str):
    from win32com.client import Dispatch
    speak = Dispatch("SAPI.SpVoice")
    speak.speak(str)

if __name__ == '__main__':
    r = requests.get("https://newsapi.org/v2/top-headlines?country=in&category=sports&pageSize=1&apiKey=49c1df5615224f30ae11578adba12936")
    a=r.text
    y= json.loads(a) #this will convert string to python dictionary
    arts= y['articles']
    for articles in arts:
        speak('title')