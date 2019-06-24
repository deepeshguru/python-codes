from gtts import gTTS 

mytext = "Text is converted into audio"

language = 'en'

myobj = gTTS(text=mytext, lang=language, slow=False) 


myobj.save("welcome.wav")
