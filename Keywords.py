import requests
import json
from random import randrange
import os
from DateTime import getCurrentTime
from Transcript import determineTranscript


def ifAngrySad(emotions):
    if (("anger" in emotions) or ("sadness" in emotions)):
        os.system('aplay wrong.wav')
        os.system('arecord -D plughw:1,0 -d 10.0 problem.wav')
        url = 'https://stream.watsonplatform.net/speech-to-text/api/v1/recognize?model=en-US_NarrowbandModel&continuous=true&'
        username = 'd1dfc1fa-296b-42e3-b270-dc986716ae81'
        password = 'ocNLsfGfVLgv'

        headers = {"Content-Type": 'audio/wav'}

        audio = open('speak.wav', 'rb')

        r = requests.post(url=url, data=audio, headers=headers, auth=(username, password))

        text_file = open("WatsonSTTResult.txt", "w")
        text_file.write(r.text)
        text_file.close()
        transcript = determineTranscript()

        serverUrl = "https://bears.localtunnel.me/addtranscript"
        date = getCurrentTime()
        data = {"Date": date, "Transcript": transcript}

        r = requests.post(serverUrl, data=json.dumps(data))

        randPlat()

    os.system('aplay joke.wav')
    randJoke()

def randPlat():
        num = randrange(0, 10, 1)
        arr = ['aplay p1.wav', 'aplay p2.wav', 'aplay p3.wav', 'aplay p4.wav', 'aplay p5.wav', 'aplay p6.wav', 'aplay p7.wav', 'aplay p8.wav', 'aplay p9.wav', 'aplay p10.wav',]
        line = arr[num]
        os.system(line)

def randJoke():
        num = randrange(0, 10, 1)
        arr = ['aplay joke1.wav', 'aplay joke2.wav', 'aplay joke3.wav', 'aplay joke4.wav', 'aplay joke5.wav', 'aplay joke6.wav', 'aplay joke7.wav', 'aplay joke8.wav', 'aplay joke9.wav', 'aplay joke10.wav',]
        line = arr[num]
        os.system(line)
