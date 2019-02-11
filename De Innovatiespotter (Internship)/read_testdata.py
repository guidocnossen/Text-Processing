#De Innovatiespotter
#@guido cnossen
#g.cnossen.1@innovatiespotter.nl

import ezodf
import sys
import re

def remove_punctuation(words):
	
	# Remove punctuation from list of tokenized words
	# original code for this function from source: https://www.kdnuggets.com/2018/03/text-data-preprocessing-walkthrough-python.html
	
	new_words = []
	query_words = []
	for word in words:
		if '#' in word:
			new_word = re.sub("\.",'',word)
			new_word = re.sub('##hls##', '', new_word)
			new_word = re.sub('##hle##', '', new_word)
			new_word = re.sub(r'[^\w\s]', '', new_word)
			query_words.append(new_word)
			if new_word != '':
				new_words.append(new_word)
		else:
			new_word = re.sub(r'[^\w\s]', '', word)
			if new_word != '':
				new_words.append(new_word)
				
	return new_words, query_words
	
def main(argv):
	
	# open excel file with Trefwoorden --
	doc = ezodf.opendoc(argv[1])

	print('opening excel file and defining column- and row values...')
	for sheet in doc.sheets:		
		lines_list = []
		companies = []
		highlights = []
		for row in sheet.rows():
			row_list = []
			for cell in row:
				row_list.append(cell.value)
			companies.append(row_list[1])
			highlights.append(row_list[2])
		companies = companies[1:-2]	
		highlights = highlights[1:-2]																							
		highlight = []
		matching = []
		for i in highlights:
			i = i.lower()
			words = i.strip().split()
			words, query_words = remove_punctuation(words)
			highlight.append(words)	
			matching.append(query_words)
		combined = list(zip(companies,highlight,matching))
		print(combined[:10])
		
	with open('data/Topsectoren/' + '{0}.txt'.format(argv[1][:-4]), 'w') as f:
		for line in combined:
			f.write(str(line[0]) + '\t')
			for word in line[1]:
				f.write(str(word) + ' ')
			f.write('\t')
			for word2 in line[2]:
				f.write(str(word2) + ' ')
			f.write('\n')
		print('Done')
		f.close()
		
		

if __name__== '__main__':
	main(sys.argv)
