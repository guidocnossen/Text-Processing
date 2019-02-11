import spacy
import itertools
from nltk.corpus import comtrans
from nltk.translate import AlignedSent, Alignment
nlp = spacy.load('nl_core_news_sm')
dutch_lines=[]
fr_lines= []
with open('frysian_data.txt', 'r',  encoding="utf-8") as friesfile:
	for lines in friesfile:
			fr_lines.append(lines)

	with open('translated_frysian_data.txt', 'r',  encoding="utf-8") as dutchfile:
		for lines in dutchfile:
			dutch_lines.append(lines)


for i,y in itertools.zip_longest(dutch_lines,fr_lines):
	identical_index = []
	algnsent = AlignedSent(i,y)
	#print(algnsent.words,algnsent.mots)
	#print(len(algnsent.words.split()),len(algnsent.mots.split()))
	dutch_list = algnsent.words.split()
	frysian_list = algnsent.mots.split()
	du_fr_list = []
	if len(dutch_list) == len(frysian_list):
		dutch_word = []
		frysian_word = []
		idenNew = [i,y]
		identical_index.append(idenNew)
		#print(identical_index[0][0])
		#print(identical_index[0][1])
		#print(len(identical_index), identical_index)
		for words, words2 in identical_index:
			for word in words.split():
				dutch_word.append(word)
			for word2 in words2.split():
				frysian_word.append(word2)
			du_fr_list = zip(dutch_word, frysian_word)
			for i in du_fr_list:
				print(i)
	else:
		dutch_word = []
		frysian_word = []
		idenNew = [i,y]
		identical_index.append(idenNew)
		for words, words2 in identical_index:
			for word in words.split():
				dutch_word.append(word)
			for word2 in words2.split():
				frysian_word.append(word2)
		#print(dutch_word, frysian_word)
		if dutch_word[0][0] == frysian_word[0][0]:
			du_fr_list = zip(dutch_word, frysian_word)
			for i in du_fr_list:
				print(i)
		
		
		
		
		
		










		#with open('ud_parsed.txt', 'r',  encoding="utf-8") as parsedfile:
			#for dutch, fries in zip(dutchfile,friesfile):
			#	dutch = dutch.rstrip()
			#	fries = fries.rstrip()
			#	fr_doc = nlp(fries)
			#	nl_doc = nlp(dutch)
			#	for fr_token in fr_doc:
			#		for nl_token in nl_doc:
			#			nl_dependency=(nl_token.text, nl_token.dep_,[child for child in nl_token.children])
						#fr_dependency=(fr_token.text, fr_token.dep_,[child for child in fr_token.children])
			#			print(nl_dependency, fr_token)					
					

				#for nl, fr,ud in zip(dutch.split(), fries.split(),parsedfile):
					#print(nl,"|",fr,"|",ud)



