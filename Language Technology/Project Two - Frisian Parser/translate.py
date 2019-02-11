
from translate_api.translate_api import api
import json

with open('frysk_data_kopie.json', 'r') as f:
    array = json.load(f)

translated = []

for text in array:
	frisian_text = text['content']
	translated.append(frisian_text+"\n")


	# dutch_text = api(text=frisian_text,from_language='fy',to_language='nl',host='https://translate.google.cn', proxy=None)
	# print(dutch_text)
	# translated.append(dutch_text + "\n")



print("bezig met schrijven")
with open('frysian_data.txt', 'w',  encoding="utf-8") as outfile:
	for sentences in translated:
		outfile.write(sentences)