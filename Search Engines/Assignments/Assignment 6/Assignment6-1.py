#!/usr/bin/env python
# Guido Cnossen

import sys

def main(argv):
	
	# eerste stukje code: http://stackoverflow.com/questions/10507104/row-to-column-transposition-in-python
	# probability matrix wordt gegenereerd op basis van een input file
	
	probability_matrix = []
	with open(argv[1]) as f:  
		lis = [x.split() for x in f]
		for x in zip(*lis):
			probability_matrix.append(x)
	
	
	# vervolgens wordt x0 op [1,0,0....] gesteld afhangende van het aantal kolommen in de probability matrix	
	# aan de hand daarvan wordt de calculatie van de vectors gestart
	
	# !!!!!! Het programma kan bijgesteld worden voor een output van alle berekende vectors door de ''' symbolen te verwijderen.!!!!!!#	
	x_0 = [1]
	for i in probability_matrix:
		x_0.append(0)
	del x_0[-1]
	x_list = [0,1]
	count = 0
	
	while x_list[count] != x_list[count-1]:
		x_temp = []
		for row in probability_matrix:
			tempscore = 0
			for i in range(len(row)):
				tempscore += float(row[i])*x_0[i]
			x_temp.append(round(tempscore,4))
		x_0 = x_temp
		x_list.append(x_0)
		count += 1
	
	calculated_vectors = []
	
	for i in x_list[2:]:
		if i not in calculated_vectors:
			calculated_vectors.append(i)
	'''count = 1	
	#for i in calculated_vectors:
		#print("Vector X_{}: {}".format(count,i))
		#count += 1'''
	
	print("PageRank Vector:", calculated_vectors[-1])	
	
if __name__ == "__main__":
	main(sys.argv)
			
		
		
		
