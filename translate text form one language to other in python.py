from googletrans import Translator

translator = Translator()

text = "Hello"

translated_text = translator.translate(text, dest="Hi").text

print(translated_text)
