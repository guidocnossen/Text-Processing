#!/usr/bin/python
# Guido Cnossen 

import sys

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

def main(argv):
	
	'''for line in sys.stdin:
		word = line.split()[0]'''
	
	for line in sys.stdin:
		w1 = line.split()[0]
		w2 = line.split()[1]
	
		print(jaccard(w1,w2))
	
	


if __name__ == '__main__':
	main(sys.argv)
