#!/usr/bin/python
# Guido Cnossen 

import urllib
import sys
import json
from collections import defaultdict

def tokenize_lowercase(tokens):
	
	tokens2 = []
	tokens_new = []
	strip_items = [".",",","!","$","%","^","&","*","(",")","/"," ","\n","\t", ":", ";", '"',"-","?"] 
	for i in tokens:
		i = i.lower()
		for j in strip_items:
			i = i.strip(j)
			
		tokens2.append(i)
	
	for i in tokens2:
		for j in strip_items:
			i = i.strip(j)
			
		tokens_new.append(i)
	
	return tokens_new
	
def main(argv):
	json_files = []
	text = open(argv[1],'r')
	for lines in text:
		line = lines.split()
		for x in line:
			x = x[36:]
			json_files.append(x)
	
	number = 0
	with open("tweets.txt", "w") as text_file:
		for map in json_files:
			tweet = []
			f = open("users_id/" + map)
			json_file = f.read()
			data = json.loads(json_file)
			tweets = data['tweets'].keys()[0:5]
			for i in tweets:
				tweet_text = data['tweets'][i]['text']
				tweet_text = tweet_text.encode('utf-8')
				tweet_text = tweet_text.split()
				tweet_text = tokenize_lowercase(tweet_text)
				text_file.write(str(number) + " ")
				number += 1
				for i in tweet_text:
					text_file.write((i) + " ")
				text_file.write("\n")
				
	text.close()
	f.close()

		
if __name__ == "__main__":
	main(sys.argv)
