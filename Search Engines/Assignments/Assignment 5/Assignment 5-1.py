#!/usr/bin/env python3
# Guido Cnossen
#S2610833


import sys

from collections import defaultdict

def kappa(PA,PE):
	
	kappa_score = (PA - PE) / (1 - PE)
	kappa_score = float("{0:.4f}".format(kappa_score))
	
	PA = float("{0:.4f}".format(PA))
	PE = float("{0:.4f}".format(PE))
	
	return PA, PE, kappa_score
	
def main(argv):
	
	text = open(argv[1],'r')
	agreed_terms = 0
	total = 0
	
	dic = {}
	dic = defaultdict(lambda:0, dic)
	
	for line in text:
		total += 2
		line = line.split()
		dic[line[0]] += 1
		dic[line[1]] += 1
		if line[0] == line[1]:
			agreed_terms += 1
	
	PA = agreed_terms / (total / 2)
	PE = 0
	
	for i,j in dic.items():
		PE += (j / total) * (j / total)	
		
	print(kappa(PA,PE))
	
if __name__ == "__main__":
	main(sys.argv)
