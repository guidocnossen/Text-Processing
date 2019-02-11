import spacy
from nltk.tokenize import word_tokenize
import itertools
import nltk
from nltk.tag import PerceptronTagger

def replace(word):
	words =[]
	with open('translated_frysian_data.txt', 'r',  encoding="utf-8") as infile:
		for sentence in infile:
			for i in sentence.split():
				print(i)
				words.append(i)
	for y in words:
		lol = word.replace(word,i)
		# print(lol)

nlp = spacy.load('nl_core_news_sm')
parsed = []
whole_sen=[]
fr=[]
with open('translated_frysian_data.txt', 'r',  encoding="utf-8") as infile:
	for sentence in infile:
		#sentence= sentence.rstrip()
		doc = nlp(sentence)
		for token in doc:
			dependency = [token.text, token.dep_,
         	token.shape_, token.is_alpha, token.is_stop,[child for child in token.children]]
			
			
			if dependency[0] == "\n":
				whole_sen.append(parsed)
				parsed=[]

			else:
				parsed.append(dependency)

frysian=[]
tagger = PerceptronTagger()
with open('frysian_data.txt', 'r',  encoding="utf-8") as fr_infile:
	for sentence in fr_infile:
		sentence = word_tokenize(sentence)
		pos = tagger.tag(sentence)
		
		fr.append(pos)
other=[]
final =[]
fr_longer=[]
for k in range(len(fr)):
	fries = fr[k]
	parsed = whole_sen[k]
	if len(fries) == len(parsed):
		for words, fr_words in zip(parsed,fries):
			print(words[0])
			other.append(words)
			# print(fr_words[0])
			words[0]=fr_words
			final.append(words)
			# print(words)


	elif len(fries) > len(parsed):
		diff = (len(fries) -len(parsed))
		dum =["dummy value"]
		for dummy in range(diff):
			parsed.append(dum)
		# for fr_words, words in itertools.zip_longest(fries,parsed):
		# 	print(words,fr_words)
			# if words[0] == fr_words:
			# 	words[0] = fr_words
			# 	fr_longer.append(words)
			# else:
				
			# 	fr_longer.append(words)

		# 	if words is None:
		# 		words = "Dummy value"
		# 		fr_longer.append (words)
		# 		print(words, fr_words)
		# 	else:
		# 		fr_longer.append(words)
		# 		print(words, fr_words)
			# 	if fr_words == words[0]:
			# 		words[0]=fr_words
			# 		final.append(words)
			# 	else:
			# 		if  words[0][0:1]==fr_words[0:1] and words[0][-1:]==fr_words[-1:]:
			# 			words[0]=fr_words
			# 			final.append(words)
			# 		else:
			# 		# 	print(words[0],fr_words)
	# else: 
	# 	diff = (len(fries) -len(parsed))
	# 	for words, fr_words in itertools.zip_longest(parsed,fries) :
	# 		if words[1] != "det" and words[1] != "case" and words[1] != "cop" and words[1] != "advmod" :

				# print(words,fr_words)
	# 		if  words[0]== fr_words:
	# 			print(words[0], fr_words)
	# 		else: 
	# 			fr_words[index] + 1

# print(other)
# with open('standard.txt', 'w',  encoding="utf-8") as outfile:
# 	for i,y in zip(other,final):

# 		outfile.write(str(i))
# 		outfile.write(" | ")
# 		outfile.write(str(y))
# 		outfile.write("\n")

# for i in other:
#  	print(i)

	# else:
	# 	print("langer")
	# 	print(len(fries),len(parsed))

	# 	# word = parsed[0][0]
	# 	print(fries[k])
		
