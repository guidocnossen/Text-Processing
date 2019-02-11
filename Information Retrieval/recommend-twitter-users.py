#!/usr/bin/env python3
# Guido Cnossen

from collections import Counter
import json
import collections
import sys


# SLOPE ONE METHOD!!!!
def V3(l1,l2):
	# function that defines which followers of a user can be saved to the v3 list and thus get a score of + 1. 
	V3_list = []
	new_list = l1 + l2
	new_list2 = [item for item, count in collections.Counter(new_list).items() if count > 1]
	
	if len(new_list2) >= 0:
		for i in new_list:
			if i not in l1:
				V3_list.append(i)
			else:
				return V3_list
	
	return V3_list
	
def main(argv):
	# open the file from the user_followers function
	f = open('user_followers.json', 'r')
	data = json.load(f)
	data2 = []
	index = 0
	for i in data:
		data2.append(i)
	
	# compare the followers of one user to the followers of the other users
	while index != len(data):
		V3_list = []
		for i in data:
			i = data[index]
			for j in data2:
				for k in i:
					for h in j:
						user = k
						user2 = h
						followers = i[k]
						followers2 = j[h]
						'''print(user)
						print(user2)
						print(followers)
						print(followers2)'''
						V3_list = V3_list + V3(followers, followers2)
		results = top_10_v3 = Counter(V3_list).most_common(10)
		#write top 10 of recommended followers for each user to an outputfile
		with open('results.txt', 'w') as output:
			output.write(str(results) + '\n')
			print('line written')
			index + 1
	
		#This program does not produce the desired outputfile, I dont know why but it is taking really long...
if __name__ == '__main__':
	main(sys.argv)
