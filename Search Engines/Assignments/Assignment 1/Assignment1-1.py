#!/usr/bin/env python3
# Guido Cnossen
# s2610833

import pickle
import sys
from collections import defaultdict

def main(argv):
	
	ex_tweets = pickle.load(open('ex_tweets.pickle','rb'))
	for i, j in ex_tweets.items():
		post2 = defaultdict(list)
		words = j[2].split()
		count = 0
		for word in words:
			post2[word].append(words.index(word))
			words[count] = ""
			count += 1
		for i,j in post2.items():
			print(i,j)


if __name__ == "__main__":
	main(sys.argv)
