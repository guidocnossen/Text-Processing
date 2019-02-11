#!/usr/bin/python
# Guido Cnossen 
#s2610833

import sys
import pickle
import math
import operator

def term_frequency(w1,w2):
	
	frequency_word = 0 
	w1 = w1.lower()
	w2 = w2.lower()
	w1 = w1.strip('!?.,!@#$%^&*()')
	w2 = w2.strip('!?.,!@#$%^&*()')
	
	if w1 == w2:
		frequency_word = frequency_word + 1
		
	else:
		frequency_word = frequency_word + 0
	
	return frequency_word
	
	
def main(argv):
	
	docs = pickle.load(open('docs.pickle','rb'))
	post = pickle.load(open('post.pickle', 'rb'))
	
	
	# Het programma kijkt of er 1 of 2 termen ingevoerd worden door de gebruiker. 
	# Op basis daarvan wordt de output van tweets met de betreffende querytermen geleverd
				#Als er twee query termen ingevoerd worden door de gebruiker, laat het programma de tweets zien met beide termen, de tweets met alleen
				#de eerste term en de tweets met alleen de laatste term. Achter de tweets staan de TF_IDF scores gegeven. 
	
	
	for line in sys.stdin:
		inp = line.split()
		N = len(docs)
		DF = 0
		IDF = 0 
		TF_IDF = 0
		results = []
		results_both = []
		results_first_term = []
		results_second_term = []
				
		if len(inp) == 1:
			w1 = line.split()[0]
			intersect_set = post[inp[0]]
			for tweets in intersect_set:
				results.append(docs[tweets][1])
			
			one_word = []
			DF = len(results)
			IDF = math.log(N/DF)
			for i in results:
				TF = 0
				TF_scores = []
				for w in i.split():
					TF_scores.append(term_frequency(w,w1))			
				for scores in TF_scores:
					if scores == 1: 
						TF = TF + 1
					else:
						TF = TF + 0		

				TF_IDF = TF * IDF
				i = (i , TF_IDF)
				one_word.append(i)
			
			print(sorted(one_word, key=lambda element: element[1], reverse=True))

				
		if len(inp) == 2:
			w1 = line.split()[0]
			w2 = line.split()[1]
			aset = post[inp[0]]
			bset = post[inp[1]]
			intersect_set = aset & bset
			for tweets in intersect_set:	
				results_both.append(docs[tweets][1])
				print('Documents with Both Queryterms:')
				print()
			
			two_word = []
			DF = len(results_both)
			IDF = math.log(N/DF)
			for i in results_both:
				TF1 = 0
				TF2 = 0
				TF1_scores = []
				TF2_scores = []
				for w in i.split():
					TF1_scores.append(term_frequency(w,w1))
					TF2_scores.append(term_frequency(w,w2))
				for scores in TF1_scores:
					if scores == 1: 
						TF1 = TF1 + 1
					else:
						TF1 = TF1 + 0 
				for scores in TF2_scores:
					if scores == 1:
						TF2 = TF2 + 1
					else:
						TF2 = TF2 + 0
	
				TF = TF1 + TF2
				TF_IDF = TF * IDF
				i = (i, TF_IDF)
				two_word.append(i)
			
			print(sorted(two_word, key=lambda element: element[1], reverse=True))
				
			print()
			
			for tweets in aset:
				results_first_term.append(docs[tweets][1])
			print('Documents with only the First Queryterm:')
			print()
			
			first_term = []
			DF = len(results_first_term)
			IDF = math.log(N/DF)
			for i in results_first_term:
				TF3 = 0
				TF3_scores = []
				for w in i.split():
					TF3_scores.append(term_frequency(w,w1))
				for scores in TF3_scores:
					if scores == 1: 
						TF3 = TF3 + 1
					else:
						TF3 = TF3 + 0 
			
				TF_IDF = TF3 * IDF
				i = (i, TF_IDF)
				first_term.append(i)	
			
			print(sorted(first_term, key=lambda element: element[1], reverse=True))	
			
			print()	
			for tweets in bset:
				results_second_term.append(docs[tweets][1])
				print('Documents with only the Second Queryterm:')
				print()
			
			second_term = []
			DF = len(results_second_term)
			IDF = math.log(N/DF)
			for i in results_second_term:
				TF4 = 0
				TF4_scores = []
				for w in i.split():
					TF4_scores.append(term_frequency(w,w2))
				for scores in TF4_scores:
					if scores == 1: 
						TF4 = TF4 + 1
					else:
						TF4 = TF4 + 0 
				
				TF_IDF = TF4 * IDF
				i = (i, TF_IDF)
				second_term.append(i)	
			
			print(sorted(second_term, key=lambda element: element[1], reverse=True))	



if __name__=='__main__':
	main(sys.argv)
