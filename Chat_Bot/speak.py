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

import win32com.client as wincl

def speak(str):
    from win32com.client import Dispatch
    n=1
    speaker_number = n
    speak = wincl.Dispatch("SAPI.SpVoice")
    vcs = speak.GetVoices()
    SVSFlag = 11
   # print(vcs.Item (speaker_number) .GetAttribute ("Name")) # speaker name
    speak.Voice
    speak.SetVoice(vcs.Item(speaker_number))
    #SAPI.Voice = SAPI.getvoices.item(1)
    print(f"Bumble_B : {str}")
    speak.Speak(str)
