import speech_recognition as sr

r = sr.Recognizer()



audio_file = sr.AudioFile('test_audio.wav')

with audio_file as source:
   audio = r.record(source)
   
mytext = r.recognize_google(audio)
print(mytext)
