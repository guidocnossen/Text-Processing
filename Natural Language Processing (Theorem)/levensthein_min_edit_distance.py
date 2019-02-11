cd#!/usr/bin/env python3
# Guido Cnossen

import sys

def levensthein_distance(w1, w2):
	#based on the algortihm on page 59 of the handbook 
	wl1 = len(w1)
	wl2 = len(w2)
	
	# determine the vowels in a list
	vowels = ["a","e","i","o","u"]
	
	lev_dis = [[0 for i in range(wl2+1)] for j in range(wl1+1)]
	for i in range(wl1+1):
		if w1[i-1] in vowels:
			lev_dis[i][0] = i - 0.5
		else:
			lev_dis[i][0] = i
	for i in range(wl2+1):
		lev_dis[0][i] = i
	for i in range(1, wl1+1):
		for j in range(1, wl2+1):
			if w1[i-1] in vowels:
				if w1[i-1] == w2[j-1]:
					lev_dis[i][j] = lev_dis[i-1][j-1]
				else:
					lev_dis[i][j] = 0.5 + min(lev_dis[i-1][j], lev_dis[i][j-1]) 
			elif w2[j-1] in vowels:
				if w1[i-1] == w2[j-1]:
					lev_dis[i][j] = lev_dis[i-1][j-1]
				else:
					lev_dis[i][j] = 0.5 + min(lev_dis[i-1][j], lev_dis[i][j-1]) 
			else:
				if w1[i-1] == w2[j-1]:
					lev_dis[i][j] = lev_dis[i-1][j-1]
				else:
					lev_dis[i][j] = 1 + min(lev_dis[i-1][j], lev_dis[i-1][j-1], lev_dis[i][j-1]) 
					
	return lev_dis[wl1][wl2]
	
def main(argv):
	
	for line in sys.stdin:
		w1 = line.split()[0]
		w2 = line.split()[1]
		print(levensthein_distance(w1,w2))
		
if __name__ == "__main__":
	main(sys.argv)
