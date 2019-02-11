#!/usr/bin/env python3
# Guido Cnossen

from collections import defaultdict
import pickle
import sys


def main(argv):
	
	db = defaultdict(list)
	docs = pickle.load(open('docs.pickle','rb'))
	for i,j in docs.items():
		
		words = j[2].split()
		count = 0
		for word in words:
			if i in db[word]:
				db[word].append(sorted(index(word)))
			else:
				db[word].append([i, words.index(word)])
			words[count] = ""
			count += 1
			
	for i,j in db.items():
		print(i,j)
			
	with open('db.pickle','wb') as f:
		pickle.dump(db, f)
		

if __name__ == "__main__":
	main(sys.argv)
