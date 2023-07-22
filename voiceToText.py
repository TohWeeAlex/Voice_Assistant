import speech_recognition as sr
import pyaudio

r = sr.Recognizer()
with sr.Microphone() as source:
    print ("speak anything :")
    audio = r.listen(source)
    request = r.recognize_google(audio)
    print (request)
