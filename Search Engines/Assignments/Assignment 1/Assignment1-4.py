#!/usr/bin/env python3
# Guido Cnossen
# s2610833

import sys
import pickle

def main(argv):
	
	docs = pickle.load(open('docs.pickle','rb'))
	post = pickle.load(open('post.pickle', 'rb'))
	db = pickle.load(open('db.pickle', 'rb'))
	
	for line in sys.stdin:
		words = line.split()
		word1 = words[0]
		word2 = words[1]
		
		l1 = db[word1]
		l2 = db[word2]
		
		aset = post[word1]
		bset = post[word2]
		inter_set = aset & bset
		
		for i in l1:
			for j in l2:
				if i[0] == j[0]:
					if (i[1]+1) == j[1]:
						for tweetID in inter_set:
							print(docs[tweetID][1])
				else:
					continue
						
if __name__ == '__main__':
    main(sys.argv)
