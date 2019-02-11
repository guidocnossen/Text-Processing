#!/usr/bin/env python3
#Guido Cnossen

import json
import collections
import sys

def main(argv):

	text = open('matrix_training.csv', 'r')
	users = []
	vips = []
	for line in text:
		users.append(line.split()[0])
		vips.append(line.split()[1])
		
	data = list(zip(users,vips))
	'''users2 = [item for item, count in collections.Counter(users).items() if count > 1]'''
	user_followers = []
	'''print(len(users))
	print(len(vips))
	print(len(users2))'''
	# for every user in matrix_training.csv create a dictionary with the user and their followers in a list
	for i in users:
		user = {}
		user[] = []
		for j in data:
			if i == j[0]:
				user[i].append(j[1])
		user_followers.append(user)
	'''print(len(user_followers))'''
	# write all dictionaries of the users to a single list in an outputfile
	with open('user_follower_test.json', 'w') as output:
		json.dump(user_followers, output)			

if __name__ == '__main__':
	main(sys.argv)
