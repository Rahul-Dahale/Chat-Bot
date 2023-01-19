import json
import os
import random
import datetime
import wikipedia
import webbrowser
import pyjokes
import time
import requests
import win32com.client as wincl
from speak import speak

import speech_recognition as sr
r=sr.Recognizer()
with sr.Microphone() as source:
    print('Speak Something : ')
    audio = r.listen(source)
    try:
        text = r.recognize_google(audio)
        print('You : {}'.format(text))
    except:
        print('Sorry I could not Recognize You....Please try again')

     
    while True:
         
        query ="{}".format(text).lower()
        
        if 'wikipedia' in query or 'who is' in query or 'what is' in query:
            #speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            query = query.replace("who is", "")
            query = query.replace("what is", "")
            results = wikipedia.summary(query, sentences = 3)
            speak("According to Wikipedia")
            print(results)
            speak(results)
            r=sr.Recognizer()
            with sr.Microphone() as source:
                print('Speak Something : ')
                audio = r.listen(source)
                try:
                    text = r.recognize_google(audio)
                    print('You : {}'.format(text))
                except:
                    print('Sorry I could not Recognize You....Please try again')
 
        elif 'open youtube' in query or 'show me youtube' in query:
            speak("Here you go to Youtube\n")
            webbrowser.open("youtube.com")
            r=sr.Recognizer()
            with sr.Microphone() as source:
                print('Speak Something : ')
                audio = r.listen(source)
                try:
                    text = r.recognize_google(audio)
                    print('You : {}'.format(text))
                except:
                    print('Sorry I could not Recognize You....Please try again')
 
        elif 'open google' in query:
            speak("Here you go to Google\n")
            webbrowser.open("google.com")
            r=sr.Recognizer()
            with sr.Microphone() as source:
                print('Speak Something : ')
                audio = r.listen(source)
                try:
                    text = r.recognize_google(audio)
                    print('You : {}'.format(text))
                except:
                    print('Sorry I could not Recognize You....Please try again')
 
 

        elif 'open whatsapp' in query:
            speak("Here you go to Whatsapp\n")
            webbrowser.open("https://web.whatsapp.com/")
            r=sr.Recognizer()
            with sr.Microphone() as source:
                print('Speak Something : ')
                audio = r.listen(source)
                try:
                    text = r.recognize_google(audio)
                    print('You : {}'.format(text))
                except:
                    print('Sorry I could not Recognize You....Please try again')


        elif 'how are you' in query:
            speak("I am fine, Thank you")
            speak("How are you?, Sir!")
            r=sr.Recognizer()
            with sr.Microphone() as source:
                print('Speak Something : ')
                audio = r.listen(source)
                try:
                    text = r.recognize_google(audio)
                    print('You : {}'.format(text))
                except:
                    print('Sorry I could not Recognize You....Please try again')

        elif 'hello' in query or 'hai' in query or 'hi' in query    :
            speak("Hello sir!,Nice to meet you")
            r=sr.Recognizer()
            with sr.Microphone() as source:
                print('Speak Something : ')
                audio = r.listen(source)
                try:
                    text = r.recognize_google(audio)
                    print('You : {}'.format(text))
                except:
                    print('Sorry I could not Recognize You....Please try again')
            
 
        elif 'fine' in query or 'best' in query:
            speak("It's good to know that your fine")
            r=sr.Recognizer()
            with sr.Microphone() as source:
                print('Speak Something : ')
                audio = r.listen(source)
                try:
                    text = r.recognize_google(audio)
                    print('You : {}'.format(text))
                except:
                    print('Sorry I could not Recognize You....Please try again')
 
        elif 'whats your name' in query or 'your name' in query or 'What is your name' in query:
            speak("My friends call me Bumble B")
            
            r=sr.Recognizer()
            with sr.Microphone() as source:
                print('Speak Something : ')
                audio = r.listen(source)
                try:
                    text = r.recognize_google(audio)
                    print('You : {}'.format(text))
                except:
                    print('Sorry I could not Recognize You....Please try again')
 
        elif 'exit' in query or 'bye' in query:
            speak("Thanks for giving me your time")
            exit()
 
        elif 'good night' in query or 'sleep' in query:
            speak("Good night sir, take care")
            exit()
             
        elif 'joke' in query or 'tell me some joke' in query:
            speak(pyjokes.get_joke())
            r=sr.Recognizer()
            with sr.Microphone() as source:
                print('Speak Something : ')
                audio = r.listen(source)
                try:
                    text = r.recognize_google(audio)
                    print('You : {}'.format(text))
                except:
                    print('Sorry I could not Recognize You....Please try again')
             
 
        elif 'search' in query or 'play' in query:
             
            query = query.replace("search", "")
            query = query.replace("play", "")         
            webbrowser.open(query)
            r=sr.Recognizer()
            with sr.Microphone() as source:
                print('Speak Something : ')
                audio = r.listen(source)
                try:
                    text = r.recognize_google(audio)
                    print('You : {}'.format(text))
                except:
                    print('Sorry I could not Recognize You....Please try again')
 
        elif 'who i am' in query:
            speak("If you talk then definitely your human.")
            r=sr.Recognizer()
            with sr.Microphone() as source:
                print('Speak Something : ')
                audio = r.listen(source)
                try:
                    text = r.recognize_google(audio)
                    print('You : {}'.format(text))
                except:
                    print('Sorry I could not Recognize You....Please try again')



        elif 'what do you look like?' in query or 'your look' in query or 'explain yourself' in query or 'yourself' in query:
            speak("Imagine the feeling of a friendly hug combined with the sound of laughter. Add a librarian's love to books, mix in sunny disposition and a dash of unicorn sparkles, and voila! ")
            r=sr.Recognizer()
            with sr.Microphone() as source:
                print('Speak Something : ')
                audio = r.listen(source)
                try:
                    text = r.recognize_google(audio)
                    print('You : {}'.format(text))
                except:
                    print('Sorry I could not Recognize You....Please try again')
 
        elif 'pyaar kya hai?' in query:
            speak("It is 7th sense that destroy all other senses")
            r=sr.Recognizer()
            with sr.Microphone() as source:
                print('Speak Something : ')
                audio = r.listen(source)
                try:
                    text = r.recognize_google(audio)
                    print('You : {}'.format(text))
                except:
                    print('Sorry I could not Recognize You....Please try again')
 
        elif 'do you have an imagination' in query + "?":
            speak("I'm imagining being covered in a pile of puppies. It's the cutest pile ever")
            r=sr.Recognizer()
            with sr.Microphone() as source:
                print('Speak Something : ')
                audio = r.listen(source)
                try:
                    text = r.recognize_google(audio)
                    print('You : {}'.format(text))
                except:
                    print('Sorry I could not Recognize You....Please try again')

 
        elif "good morning" in query or "good evening" in query or "good afternoon" in query:
            speak(query + " Sir")
            speak("How are you Sir")
            r=sr.Recognizer()
            with sr.Microphone() as source:
                print('Speak Something : ')
                audio = r.listen(source)
                try:
                    text = r.recognize_google(audio)
                    print('You : {}'.format(text))
                except:
                    print('Sorry I could not Recognize You....Please try again')
 

        elif "who are you" in query:
            speak("I am your Virtual Voice Assistant")
            r=sr.Recognizer()
            with sr.Microphone() as source:
                print('Speak Something : ')
                audio = r.listen(source)
                try:
                    text = r.recognize_google(audio)
                    print('You : {}'.format(text))
                except:
                    print('Sorry I could not Recognize You....Please try again')

        
