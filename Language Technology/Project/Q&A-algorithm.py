from SPARQLWrapper import SPARQLWrapper, JSON
from lxml import etree
import sys, socket

def main(argv):
	for line in sys.stdin:
		found = 0
		try:
			sentence = filter_input(line)
			XY_nodes, SPARQL_prop = choose_node(sentence)
			for node in XY_nodes:
				if found == 0:
					X,Y = pick_X_Y(sentence,node[0],node[1])
					X = get_lemma(X)
					found = create_and_fire_query(X,Y,SPARQL_prop)
			if found == 0:
				print("\nYour question could not be answered\n")
		except:
			print("\nYour question could not be answered\n")
		
		
		
	
def filter_input(line):
	line = line.rstrip()
	sentence = 	line[0].lower() + line[1:]
	if sentence[-1] == "?":
		sentence = sentence[:-1]
	return sentence

def choose_node(sentence):
	sentence = sentence.split()
	SPARQL_prop = ""
	
	Y_nodes = []
	X_nodes = []
	
	if "wie" == sentence[1]:
		Y_nodes.append('//node[@rel="su" and @cat="np"]')
		X_nodes.append('//node[@rel="hd" and @pt="ww"]')
		if sentence[-1] == "geopend":
			SPARQL_prop = "opener"
		elif sentence[-1] == "georganiseerd":
			SPARQL_prop = "organisator"
		elif sentence[-1] == "gedragen":
			SPARQL_prop = "vlam"
		
		
	if sentence[0] == "wie" or sentence[0] == "wat" and sentence[1] == "is" or sentence[1] == "zijn" or sentence[1] == "was" or sentence[1] == "waren":
		Y_nodes.append('//node[@rel="obj1"]')
		X_nodes.append('//node[@rel="hd" and @pt="n"]')
	
	if sentence[0] == "hoeveel":
		Y_nodes.append('//node[@rel="obj1" and @cat="np"]')
		X_nodes.append('//node[@rel="hd" and @pt="n"]')
		
	if sentence[0] == "hoe" and len(sentence) <7:
		Y_nodes.append('//node[@rel="su" and @cat="mwu"]')
		X_nodes.append('//node[@rel="hd" and @pt="adj"]')
		
	if sentence[0] == "welke" or sentence[1] == "welke":
		Y_nodes.append('//node[@cat="mwu"]')
		X_nodes.append('//node[@rel="hd" and @pt="n"]')
		
	if sentence[0] == "waar":
		Y_nodes.append('//node[@rel="su"]')
		X_nodes.append('//node[@rel="hd" and @pt="ww"]')
	
	if sentence[1] == "welke":
		Y_nodes.append('//node[@rel="su" and @cat="np"]')
		X_nodes.append('//node[@rel="obj1" and @cat="np"]')
		
	if sentence[1] == "welke":
		Y_nodes.append('//node[@cat="mwu"]')
		X_nodes.append('//node[@rel="obj1" and @cat="np"]')
	
		
	else:
		Y_nodes.append('//node[@spectype="deeleigen"]')
		X_nodes.append('//node[@rel="hd"and@pt="n"]')
	
	SPARQL_prop = SPARQL_prop.split()
	
	XY_nodes = []
	counter = 0
	for node_X in X_nodes:
		XY_nodes.append((node_X,Y_nodes[counter]))
		counter += 1
	
	print("nodes:",XY_nodes,"Prop:",SPARQL_prop)		
	return XY_nodes, SPARQL_prop
	
def pick_X_Y(sentence,node_X,node_Y):
	"""Vind X en Y"""
	xml = alpino_parse(sentence)
	names_Y = xml.xpath(node_Y)
	Y = []
	for name in names_Y :
		Y.append(tree_yield(name))
	Y = Y[0].split()
	if Y[0] == "de" or Y[0] == "het" or Y[0] == "een":
		del Y[0]
	Y = " ".join(Y)
	
	X =[]
	names_X = xml.xpath(node_X)
	for name in names_X :
		X.append(tree_yield(name))
	X = " ".join(X)
	X = X.lower()
	Y = Y.lower()
	print("X:"+X+"\n"+"Y:"+Y)
	return X,Y

def create_and_fire_query(X,Y,SPARQL_prop):
	link = ""
	link_list = []
	#X = X[1]
	f= open('pairCounts', 'r')
	for line in f:
		line = line.split("	")
		Y_pairCounts = line[0].lower()
		if Y_pairCounts == Y:
			link_list.append(line)
	
	highest_freq = 0
	for l in link_list:
		if int(l[2]) > highest_freq:
			link = l[1]
			highest_freq = int(l[2])
	print("link:"+link)
	answers = []
	found = 0
	if SPARQL_prop == []:
		SPARQL_prop = get_prop(X)
	for prop in SPARQL_prop:
		if found == 0:
			SPARQL_Query = "SELECT ?antwoord WHERE {} <{}> prop-nl:{} ?antwoord {}".format('{',link,prop,'}')
			print("Query:",SPARQL_Query)
			sparql = SPARQLWrapper("http://nl.dbpedia.org/sparql")
			sparql.setQuery(SPARQL_Query)	
			sparql.setReturnFormat(JSON)
			results = sparql.query().convert()
			if results["results"]["bindings"] != []:
				found += 1
			for result in results["results"]["bindings"]:
				for arg in result:
					answer = arg + " : " + result[arg]["value"]
					answers.append(answer)
	print(answers)
	return found

def get_prop(X):
	SPARQL_prop = []
	for x in X:
		f= open('GetProp', 'r')
		for line in f:
			line = line.strip()
			line = line.split('#')
			if x in line and line[-1] not in SPARQL_prop:
				SPARQL_prop.append(line[-1])
	if SPARQL_prop == []:
		SPARQL_prop = X
	print("prop:",SPARQL_prop)
	return SPARQL_prop

def get_lemma(word):
	xml = alpino_parse(word)
	leaves = xml.xpath('descendant-or-self::node[@word]')
	words = []
	for l in leaves :
		words.append(l.attrib["lemma"])
	word = word.split()[-1]
	#if len(words) > 1:
	words = (words[-1],word)
	print("lemma:",words)
	return words

def tree_yield(xml):
	"""Van nestor"""
	leaves = xml.xpath('descendant-or-self::node[@word]')
	words = []
	for l in leaves :
		words.append(l.attrib["word"])
	return " ".join(words)
		

def alpino_parse(sent, host='zardoz.service.rug.nl', port=42424):
	s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
	s.connect((host,port))
	sent = sent + "\n\n"
	sentbytes= sent.encode('utf-8')
	s.sendall(sentbytes)
	bytes_received= b''
	while True:
		byte = s.recv(8192)
		if not byte:
			break
		bytes_received += byte
	#    print(bytes_received.decode(’utf-8’), file=sys.stderr)
	xml = etree.fromstring(bytes_received)
	return xml
		
if __name__ == "__main__":
	main(sys.argv)		
		
