# coding: utf-8
from __future__ import division

import struct
import sys

FILE_NAME = "word2vec-explorer-master/schiedam-vector.bin" # outputs schiedam-vector.bin.txt // qmodus-vector.bin.txt
									 #/qmodus-vector.bin"
									 
MAX_VECTORS = 100000 #300000 # Make sure all the words and their embeddings are taken into account
FLOAT_SIZE = 4

# define output file
output_file_name = FILE_NAME + ".txt"

# open embedding file and the new output file
with open(FILE_NAME, 'rb') as f, open(output_file_name, 'w') as f_out:
    
    c = None
    
    # read the header
    header = ""
    while c != "\n":
        c = f.read(1)
        header += c

	# define total number of vectors
	# define total length of vectors
    total_num_vectors, vector_len = (int(x) for x in header.split())
    num_vectors = min(MAX_VECTORS, total_num_vectors)
    
    
    # return the total amount of vectors (each vector contains one word and the corresponding embeddings)
    # return the vector size (each vector has the same length)
    print "Taking embeddings of %d words (out of %d total)" % (num_vectors, total_num_vectors)
    print "Embedding size: %d" % vector_len

	# iterate over all of the vectors
    for j in xrange(num_vectors):
		# define the words
        word = ""        
        while True:
            c = f.read(1)
            if c == " ":
                break
            word += c

		# define the embeddings 
        binary_vector = f.read(FLOAT_SIZE * vector_len)
        txt_vector = [ "%s" % struct.unpack_from('f', binary_vector, i)[0] 
                   for i in xrange(0, len(binary_vector), FLOAT_SIZE) ]
        
        # write to output text file
        f_out.write("%s %s\n" % (word, " ".join(txt_vector)))
        
        # keep track on progress
        sys.stdout.write("%d%%\r" % ((j + 1) / num_vectors * 100))
        sys.stdout.flush()
        
        if (j + 1) == num_vectors:
            break
            
print "\nDONE!"
print "Output written to %s" % output_file_name
