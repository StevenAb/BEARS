import os
import RPi.GPIO as GPIO
import time
import json
import requests
from Transcript import determineTranscript
from Transcript import determineEmotion
from ToneAnalyzer import toneAnalyzer
import Keywords


GPIO.setmode(GPIO.BCM)


GPIO.setup(23, GPIO.IN, pull_up_down=GPIO.PUD_UP)

os.system('aplay hello.wav')

while True:
    mic_state = GPIO.input(23)

    if (mic_state == False):
        print('Recording')
        os.system('arecord -D plughw:1,0 -d 5.0 speak.wav')
        print ('Retrieving Transcript')
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

        if "bye" in transcript:
            os.system('aplay bye.wav')
            os.system('sudo poweroff')
        if "false" not in transcript:
            toneAnalyzer(transcript)
            Keywords.ifAngrySad(determineEmotion())