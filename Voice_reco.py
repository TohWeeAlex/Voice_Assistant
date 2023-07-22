import speech_recognition as sr
import pyaudio
import os
import sys
import re
import webbrowser
import smtplib
import requests
import subprocess
from pyowm import OWM
import youtube_dl
import urllib
import urllib3
import json
from bs4 import BeautifulSoup as soup
import wikipedia
import random
import time
from time import strftime
import pyttsx3
import getpass

# API client library
import googleapiclient.discovery
# API information
api_service_name = "youtube"
api_version = "v3"
# API key
DEVELOPER_KEY = "AIzaSyD289E-tEclCA-V9ZWIVHlSkzjHLAOiOok"
# API client
youtube = googleapiclient.discovery.build(api_service_name, api_version, developerKey = DEVELOPER_KEY)




#login
def loginRequest():
    Rep = 0
    username = str(input("Enter username: "))
    password = str(getpass.getpass("Enter password: "))
    if username == "weepower":
        if password == "Galaxy_90910115":
            displayTxt = ("login")
            InputSelection(displayTxt)
        else:
            print("\n" + "Access denied" + "\n")
            loginRequest()
    #admin quick test
    elif username == "admin":         
        Rep = Rep + 1
        #print ("Rep count: " + str(Rep))
        displayTxt = ("login")
        InputSelection(displayTxt)
    else:
        print("\n" + "Access denied" + "\n")
        loginRequest()



#Input selection
def InputSelection(displayTxt):
    InputType = ""
    attemptCounter = 0
    choiceTxt = ("\n" + "Please enter your input preference (1 for text or 2 for voice): ")
    while (InputType) != ("voice" or "text"):
        InputType = str(input(choiceTxt))
        if (str(InputType)) == ("2"):
            if displayTxt == ("login"):
                ##Attempt counter 
                attemptCounter = 0
                displayTxt = ("\n" + "Tell me what can I help you with? :")
                assistant(MyVoiceRequest(displayTxt))
            else:
                ##Attempt counter
                attemptCounter = 0
                print ("checkpoint 1")
                MyVoiceRequest(displayTxt)
                return request
        elif (str(InputType)) == ("1"):
            if displayTxt == ("login"):
                ##Attempt counter
                attemptCounter = 0
                displayTxt = ("\n" + "What can I help you with? :")
                assistant(MyTextRequest(displayTxt))
            else:
                ##Attempt counter
                attemptCounter = 0
                #print ("checkpoint 1")
                request = MyTextRequest(displayTxt)
                return request
        else:
            ##Attempt counter
            attemptCounter = attemptCounter +1
            choiceTxt = ("\n" + "Please enter < 1 > for voice input or < 2 > for text input (Attempts: " + str(attemptCounter) + "):")
            continue
 


#Text input
def MyTextRequest(displayTxt):
    request = str(input(displayTxt))
    #print (request)
    return request


#Voice input
def MyVoiceRequest(displayTxt):
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source, duration=1)
        print (displayTxt)
        audio = r.listen(source)
        try:
            request = r.recognize_google(audio)
            print ("\n" + "you said :" + request + "\n")
        except:
            print("sorry could not recognize your voice")
            request = MyVoiceRequest("\n" + "Tell me what can I help you with? :");
        return request

    

#audio output
def aliceResponse(audio):
    ##Initialization
    engine = pyttsx3.init()
    ##Voice selection
    voices = engine.getProperty("voices")
    engine.setProperty("voice", voices[1].id)
    ##Speech rate setting
    engine.setProperty('rate', 130)
    ##speak audio passed as argument
    #for line in audio.splitlines():
    #    engine.say(audio)
    #    engine.runAndWait()
    engine.say(audio)
    engine.runAndWait()

##Youtube search function
def youtubeSearch(searchQuery):
    request = youtube.search().list(part="snippet", maxResults=10, q=str(searchQuery), order="relevance", type="video")
    response = request.execute()
    listNo = 0
    list_of_titles = []
    list_of_links = []
    print ("\n" + "#################### Search results ####################" + "\n")
    while True:
        time.sleep(1)
        try:
            print (str(listNo + 1) + ". " + (response['items'][listNo]['snippet']['title']) + "\n")
            list_of_titles.append((response['items'][listNo]['snippet']['title']))
            #print ("\n")
            list_of_links.append("https://www.youtube.com/watch?v=" + (response['items'][listNo]['id']['videoId']))
            #print ("<" + "https://www.youtube.com/watch?v=" + (response['items'][listNo]['id']['videoId']) + ">")
            listNo = listNo + 1
        except:
            print ("#################### END ####################")
            #print (list_of_links)  
            break
    displayTxt = ("\n" + "which video would you like to play? (say/type a number) : ")
    videoSelection = InputSelection(displayTxt)
    #print (str(videoSelection))
    #print ("checkpoint 2")
    ##Checking for video selection
    if ("1" or "one") in videoSelection.lower():
        titleN0 = 0
        linkNo = 0
    elif (("2" or "two") in videoSelection.lower()):
        titleN0 = 1
        linkNo = 1
    elif (("3" or "three") in videoSelection.lower()):
        titleN0 = 2
        linkNo = 2
    elif (("4" or "four") in videoSelection.lower()):
        titleN0 = 3
        linkNo = 3
    elif (("5" or "five") in videoSelection.lower()):
        titleN0 = 4
        linkNo = 4
    elif (("6" or "six") in videoSelection.lower()):
        titleN0 = 5
        linkNo = 5
    elif (("7" or "seven") in videoSelection.lower()):
        titleN0 = 6
        linkNo = 6
    elif (("8" or "eight") in videoSelection.lower()):
        titleN0 = 7
        linkNo = 7
    elif (("9" or "nine") in videoSelection.lower()):
        titleN0 = 8
        linkNo = 8
    elif (("10" or "ten") in videoSelection.lower()):
        titleN0 = 9
        linkNo = 9
    ##Return title and link
    printedTxt = "opening " + (str(list_of_titles[titleN0]))
    spokenTxt = str("opening " + (str(list_of_titles[titleN0])))
    webLink = str(list_of_links[linkNo])
    return printedTxt, spokenTxt, webLink

##Open webbrowser function
def openingWB(printedTxt, spokenTxt, webLink):
    print (str(printedTxt))
    aliceResponse(str(spokenTxt))
    time.sleep(0.5)
    webbrowser.open(str(webLink), new=1)
    displayTxt = "login"
    InputSelection(displayTxt)


def assistant(request):
    ##If statements for executing commands
    ##Opening
    request = request.lower()
    #print (request)
    if "open" in request:

        #youtube
        if "youtube" in request:

            #Searching on youtube
            if "search" in request:
                keyWords = ["open", "youtube", "search"]
                searchQuery = request.lower()
                for char in keyWords:
                    searchQuery = searchQuery.replace(char, "")
                openingWB(*youtubeSearch(searchQuery))


            #Personal music playlist
            elif "music" in request:
                print ("opening music from youtube")
                aliceResponse("opening music from youtube")
                time.sleep(0.5)
                webbrowser.open("https://www.youtube.com/watch?v=Pm0_G8Zl0ek&list=PLTVQYeox_PGLxf_hAbl8m5Ig9mYKJzB9s", new=1)
            
            #Open youtube website
            else:
                print ("opening YouTube")
                aliceResponse("opening YouTube")
                time.sleep(0.5)
                webbrowser.open("https://www.youtube.com", new=1)

        #reddit
        if "reddit" in request:
            if "search" in request:
                redditSearch = request[19:]
                print ("opening Reddit " + "searching: " + "(" + redditSearch + ")" + "\n")
                aliceResponse ("opening Reddit, searching," + redditSearch)
                time.sleep(0.5)
                webbrowser.open("https://www.reddit.com/r/" + redditSearch, new=1)
            else:
                print ("opening Reddit")
                aliceResponse("opeing Reddit")
                time.sleep(0.5)
                webbrowser.open("https://www.reddit.com", new=1)

        #VLC
        #if "music" in request:
            #openvlc = vlc.Instance()
            #player = openvlc.media_player_new()
            #media = openvlc.media_new("H:\BACKUP\music\Mako_Breathe.mp3")
            #media.get_mrl()
            #player.set_media(media)
            #player.play()

        #Whatsapp
        if "whatsapp" in request:
            print ("opening WhatsApp web" + "\n")
            aliceResponse("opening WhatsApp Web")
            time.sleep(0.5)
            webbrowser.open("https://web.whatsapp.com", new=1)

        #Google
        if "google" in request:
            if "search" in request:
                GGsearch = request[19:]
                print ("opening Google " + "searching: " + "(" + GGsearch + ")" "\n")
                aliceResponse("opening Google, searching," + GGsearch)
                time.sleep(0.5)
                webbrowser.open("https://www.google.com/search?q=" + GGsearch, new=1)
            else:
                print ("opening Google")
                aliceResponse("opening Google")
                time.sleep(0.5)
                webbrowser.open("https://www.google.com", new=1)

        #Netflix
        if "netflix" in request:
            print ("opening Netflix" + "\n")
            aliceResponse("opening Netflix")
            time.sleep(0.5)
            webbrowser.open("https://www.netflix.com", new=1)

        #Twtich
        if "twitch" in request:
            print ("opening Twitch" + "\n")
            aliceResponse("opening Twtich")
            time.sleep(0.5)
            webbrowser.open("https://www.twitch.com", new=1)

        #Color track
        if "color track" in request:
            print ("Opening Project Color Track" + "\n")
            aliceResponse("opening Color Track")
            time.sleep(0.5)
            subprocess.Popen("F:\Work_files\studies\C++\color_track\Release\color_track.exe")

        #BS4 and Request test
        if "testing" in request:
            link = requests.get("https://www.youtube.com/results?search_query=leave+it+all+behind").text
            souptxt = soup(link, 'html.parser')
            #print (souptxt.prettify())
            urllist = []
            titlelist = []
            index = 0
            for linkurl in souptxt.findAll("a", class_="yt-uix-tile-link yt-ui-ellipsis yt-ui-ellipsis-2 yt-uix-sessionlink spf-link"):
                linkurl2 = linkurl.get("href")
                titles = linkurl.get("title")
                #print (linkurl2)
                #print (titlelist)
                if "watch" in linkurl2:
                    urllist.append(linkurl2)

                titlelist.append(titles)

            for x in titlelist:
                index += 1
                print ( str(index) + "." + " " + x )





    #Closing
    if "close" in request:


        #Color track
        if "color track" in request:
            print ("closing Project Color Track" + "\n")
            aliceResponse("closing Color Track")
            time.sleep(0.5)
            os.system("taskkill /im color_track.exe")

        #Color track
        if "Google" in request:
            print ("closing google" + "\n")
            aliceResponse("closing Color google")
            time.sleep(0.5)
            os.system("taskkill /f /im chrome.exe")

    #shutdown
    if "shut down Alice" in request:
        print ("closing...")
        aliceResponse("closing")
        time.sleep(0.5)
        os.system("taskkill /f /im Python.exe")

    #disable
    if "disable" in request:
        subprocess.run(["devcon"], ["disable"], ["@USB\VID_0909&PID_001A&MI_00\8&3205DB0B&0&0000"])

    else:
        errorTxt = ("\n" + "Sorry I don't understand or that is beyond my capability...")
        print (errorTxt)
        aliceResponse (errorTxt)
        displayTxt = "login"
        InputSelection(displayTxt)


loginRequest()
