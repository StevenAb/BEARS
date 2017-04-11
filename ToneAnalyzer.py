import json
from watson_developer_cloud import ToneAnalyzerV3
from Transcript import determineEmotion

def toneAnalyzer(transcript):
    tone_analyzer = ToneAnalyzerV3(username='', password='', version='2016-05-19')
    text= transcript
    text_file = open("WatsonAnalyzerResult.txt", "w")
    text_file.write(json.dumps(tone_analyzer.tone(text=text), indent=2))
    text_file.close()
