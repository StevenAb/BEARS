import os

def determineTranscript():
    f = open('WatsonSTTResult.txt', 'r')
    transcript = ''
    confidence = ''
    num = 0
    while (True):
        text = f.readline()
        if '"confidence": ' in text:
            confidence = text[29:(len(text) - 3)]
            num = float(confidence)
            text = f.readline()
            if (num >= 0.7):
                transcript += " " + text[30:(len(text) - 3)]
        if text == '':
            break
    if (transcript == ''):
        os.system('aplay louder.wav')
        transcript = "false"
    return transcript

def determineEmotion():
    f = open('WatsonAnalyzerResult.txt', 'r')
    emotion = ''
    confidence = ''
    num = 0
    while (True):
        text = f.readline()
        if '"score": ' in text:
            confidence = text[21:(len(text) - 3)]
            num = float(confidence)
            text = f.readline()
            if (num >= 0.75):
                emotion += " " + text[24:(len(text) - 2)]
        if text == '':
            break
    return emotion