#!/usr/bin/python
# Guido Cnossen
# S2610833 

import sys
import pickle 

def trigram(word):
  trigram_list = []
  letters = []
  for letter in word:
	  letters.append(letter)

  for i in range(len(letters)-2):
	  trigram_list.append((letters[i] + letters[i+1] + letters[i+2]))
	  
  return trigram_list

def jaccard(w1, w2):
	# based on a code from http://love-python.blogspot.nl 
	l1 = []
	l2 = []
	
	for letters in w1:
		l1.append(letters)
	for letters in w2:
		l2.append(letters)
	
	s1 = set(l1)
	s2 = set(l2)
		
	n = len(s1.intersection(s2))
	jaccard_score = n / float(len(s1) + len(s2) - n) 
	
	return jaccard_score
	
def levensthein_distance(w1, w2):
	
	#based on a code from https://discuss.leetcode.com/
	len_w1 = len(w1)
	len_w2 = len(w2)
	lev_dis = [[0 for i in range(len_w2+1)] for j in range(len_w1+1)]
	for i in range(len_w1+1):
		lev_dis[i][0] = i
	for i in range(len_w2+1):
		lev_dis[0][i] = i
	for i in range(1, len_w1+1):
		for j in range(1, len_w2+1):
			if w1[i-1] == w2[j-1]:
				lev_dis[i][j] = lev_dis[i-1][j-1]
			else:
				lev_dis[i][j] = 1 + min(lev_dis[i-1][j], lev_dis[i-1][j-1], lev_dis[i][j-1])
	
	return lev_dis[len_w1][len_w2]

	
def main(argv):
	
	docs = pickle.load(open('docs.pickle','rb'))
	post = pickle.load(open('post.pickle', 'rb'))
	
	# basic manier 			
	words = []
	for k,v in post.items():
		words.append(k)
		
	for line in sys.stdin:
		lowlev = 10000000000
		word = line.split()
		
		if len(word) == 1:
			inter_set = post[word[0]]
			
			if inter_set == set():
				for i in words:
					lev = levensthein_distance(word[0], i)
					
					if lev < lowlev:
						lowlev = lev
						line = i
				print(line,'\n')
				inter_set = post[line]
			
			for tweetID in inter_set:
				print(docs[tweetID][1])
		
		else:
			print("Usage: De standaard input is maximaal 1 woord")
	
	# trigram index manier1
	'''words = []
	for k,v in post.items():
		words.append(k)
	
	for line in sys.stdin:
		lowlev = 1000000000
		word = line.split()
		tri = trigram(word[0])
		
		if len(word) == 1:
			inter_set = post[word[0]]
			if inter_set == set():
				for i in words:
					tri_two = trigram(i)
					for j in tri:
						for h in tri_two:
							lev = levensthein_distance(j,h)
							if lev < lowlev:
								lowlev = lev
								line = i
				print(line,'\n')
				inter_set = post[line]
			
			for tweetID in inter_set:
				print(docs[tweetID][1])
		
		else:
			print("Usage: De standaard input is maximaal 1 woord")'''
	
	# jaccard score manier
	'''words = []
	for k,v in post.items():
		words.append(k)
		
	for line in sys.stdin:
		lowlev = 1000000000
		word = line.split()
		
		if len(word) == 1:
			inter_set = post[word[0]]
			if inter_set == set():
				jac_list = []
				for i in words:
					jac = jaccard(word[0],i)
					jac_list.append(jac)
					if jac == max(jac_list):
						lev = levensthein_distance(word[0], i)
						if lev < lowlev:
							lowlev = lev
							line = i
				print(line, '\n')
				inter_set = post[line]
			
			for tweetID in inter_set:
				print(docs[tweetID][1])
		
		else:
			print("Usage: De standaard input is maximaal 1 woord")'''
					

			
			
if __name__=='__main__':
	main(sys.argv)
