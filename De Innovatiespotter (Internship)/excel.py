#De Innovatiespotter
#@guido cnossen
#g.cnossen.1@innovatiespotter.nl

import ezodf
import sys


def main(argv):
	
	# open excel file with Trefwoorden --
	doc = ezodf.opendoc('data/' + argv[1])

	print('opening excel file and defining column- and row values...')
	for sheet in doc.sheets:
		if sheet.name == 'Trefwoorden':
					
			lines_list = []
			for row in sheet.rows():
				row_list = []
				for cell in row:
					row_list.append(cell.value)
				row_list = row_list[1:3] + row_list[5:]
				lines_list.append(row_list)
			columns = lines_list[0]
			columns = columns[0:1] + columns[2:]
			lines_list = lines_list[3:-2]
	
	print('splitting trefwoorden...')		
	new_lines = []
	for i in lines_list:
		try:
			words = i[0] + ' ' + i[1]
			words = words.split()
			scores = i[2:]
			words2 = []
			words3 = []
			for i in words:
				if '"' in i[0:2]:
					words3.append(i)
				elif '~' in i:
					words3.append(i)
				else:
					words2.append(i)
			words4 = []
			for word in words2:
				row = [word] + scores
				new_lines.append(row)
			
			if len(words3) == 0:
				words3 = []
				words4 = []
				
			else: 
				first_word = words3[0]
				index = words3.index(first_word)
				for w in words3[0::2]:
					words4.append(' '.join(words3[index:index+2]))
					index = index + 2
				
				for wc in words4:
					row = [wc] + scores
					new_lines.append(row)
					
		except TypeError:
			words = i[0]
			words = words.split()
			scores = i[2:]
			words2 = []
			words3 = []
			for i in words:
				if '"' in i[0:2]:
					words3.append(i)
				elif '~' in i:
					words3.append(i)
				else:
					words2.append(i)
			words4 = []
			for word in words2:
				row = [word] + scores
				new_lines.append(row)
				
			if len(words3) == 0:
				words3 = []
				words4 = []
			else:
				first_word = words3[0]
				index = words3.index(first_word)
				for w in words3[0::2]:
					words4.append(' '.join(words3[index:index+2]))
					index = index + 2
				
				for wc in words4:
					row = [wc] + scores
					new_lines.append(row)

	print('writing new output file...')
	header = ''
	for i in columns:
		header = header + str(i) + '\t'
	header = header + '\n'
	with open('Trefwoordbestand_nieuw2.ods', 'w') as f:
		f.write(header)
		for line in new_lines:
			row = ''
			for part in line:
				part = str(part).replace('"',"'")
				part = str(part).replace('None', '')
				row = row +  part + '\t'
			row = row + '\n'
			f.write(row)
	f.close()
	              
if __name__== '__main__':
	main(sys.argv)
