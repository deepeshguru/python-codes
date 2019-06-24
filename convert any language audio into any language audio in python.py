import speech_recognition as sr
from gtts import gTTS 
from googletrans import Translator

r = sr.Recognizer()

audio_file = sr.AudioFile('test_audio.wav')
language = "Hi"
with audio_file as source:
   audio = r.record(source)
   
mytext = r.recognize_google(audio)

translator = Translator()

mytext = translator.translate(mytext, dest=language).text

myobj = gTTS(text=mytext, lang=language, slow=False) 

myobj.save("welcome.wav") 
