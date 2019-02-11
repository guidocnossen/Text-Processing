#De Innovatiespotter
#@guido cnossen
#g.cnossen.1@innovatiespotter.nl

import re, string, unicodedata
import nltk
from bs4 import BeautifulSoup
from nltk import word_tokenize, sent_tokenize
from nltk.corpus import stopwords
from nltk.stem import LancasterStemmer, WordNetLemmatizer

import sys

def remove_punctuation(words):
	
	# Remove punctuation from list of tokenized words
	# original code for this function from source: https://www.kdnuggets.com/2018/03/text-data-preprocessing-walkthrough-python.html
	
	new_words = []
	for word in words:
		if '+' in word or '-' in word:
			new_word = re.sub(r'[\+\-]', ' ', word)
			if new_word != '':
				new_words.append(new_word)
		else:
			new_word = re.sub(r'[^\w\s]', '', word)
			if new_word != '':
				new_words.append(new_word)
				
	return new_words
	
def remove_numbers(words):
	
	# remove numbers/digits from list of tokenized words
	# original code for this function from source: https://www.kdnuggets.com/2018/03/text-data-preprocessing-walkthrough-python.html
	
	new_words = []
	for word in words:
		if word.isdigit():
			new_word = ''
			new_words.append(new_word)
		else:
			new_words.append(word)
			
	return new_words

def main(argv):
	
	# open Trefwoorden text file
	doc = open('data/Energie2/' +  argv[1], 'r')
	print("Opening {0} ...".format(argv[1]))
	
	stripped_trefwoorden_list = []
	
	# read in the line of the opened text file 
	# tokenize lines
	# remove punctuation from lines
	lines = doc.readlines()
	for line in lines:
		line = nltk.word_tokenize(line)
		line = remove_punctuation(line)
		line = remove_numbers(line)
		stripped_trefwoorden_list.append(line)
	
	print('Writing Trefwoorden to new output file...')
	# write stripped Trefwoorden to output file
	with open('data/Energie2/' + 'new_preprocessed_' + '{0}.txt'.format(argv[1][:-4]), 'w') as f:
		for list in stripped_trefwoorden_list:
			for i in list:
				f.write(i + ' ')
			f.write('\t'+'Energie'+'\n')
	f.close()
			
	print('Done!')
	                  
if __name__== '__main__':
	main(sys.argv)
