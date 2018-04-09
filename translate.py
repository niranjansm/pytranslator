# Read a german word and translate that using google translate api
import requests
from googletrans import Translator
from datetime import datetime

now = datetime.now()
print (str(now))

translator = Translator()
while True:
	print("Please enter the german word to translate")
	german_word = raw_input()

	english_word = translator.translate(german_word, src='de')
	print("English Translation: " + english_word.text)
	print("")

