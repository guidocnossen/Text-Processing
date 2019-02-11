from xml.etree import ElementTree
from xml import etree
import re
import os
import sys
import json

#define path to directory with reddit files
def find_files(directory):

    paths = []
    for root, directories, files in os.walk(directory):
        for filename in files:
            filepath = os.path.join(root, filename)
            paths.append(filepath)
    return [path for path in paths]
    

# loop through the files
for fl in find_files("reddit"):
	ftfy_list = []
	print(fl)
	body_list = []
	first_element = 0
	other_element = 0
	last_element = 0 
	text = open(fl).readlines()
	
	#load in data object of 'body' to get the textual reddit comment information
	for line in text:
		data = json.loads(line)
		body_list.append(data["body"].split())
	
	#determine weither a comment containt instances of 'FTFY' or 'ftfy'
	for i in body_list:
		if "FTFY" in i:
			ftfy_list.append(i)
		if "ftfy" in i:
			ftfy_list.append(i)
	
	#check the indexes of the instances of 'FTFY' or 'ftfy'
	for i in ftfy_list:
		if i[-1] == 'FTFY' or i[-1] == 'ftfy':
			last_element += 1
		if i[0] == 'FTFY' or i[0] == 'ftfy':
			first_element += 1
	
	#Analyse data
	print("Total number of Reddit Comments for file...")
	print(len(ftfy_list))
	other_element = (len(ftfy_list) - (last_element + first_element))

	percentage1 = (first_element / len(ftfy_list) * 100)
	percentage2 = (other_element / len(ftfy_list) * 100)
	percentage3 = (last_element / len(ftfy_list) * 100)
	
	print("Percentages of indexes for the instances of 'FTFY' and/or 'ftfy'...")
	print()
	print("As First Element:")
	print(first_element," : ",percentage1)
	print()
	print("As Other Element:")
	print(other_element," : ",percentage2)
	print()
	print("As Last Element:")
	print(last_element," : ",percentage3)
		
		
			
	
			
	
		
			
			
		
