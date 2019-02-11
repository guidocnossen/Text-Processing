#!/usr/bin/env python3
# Guido Cnossen

import sys

def levensthein_distance(w1, w2):
	
	#based on a code from http://stackoverflow.com
	if not w1: 
		return len(w2)
	
	if not w2: 
		return len(w1)
		
	return min(levensthein_distance(w1[1:], w2[1:])+(w1[0] != w2[0]), levensthein_distance(w1[1:], w2)+1, levensthein_distance(w1, w2[1:])+1)


def main(argv):
	
	for line in sys.stdin:
		w1 = line.split()[0]
		w2 = line.split()[1]
		print(levensthein_distance(w1,w2))
		
if __name__ == "__main__":
	main(sys.argv)
