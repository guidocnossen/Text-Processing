# Guido Cnossen 

import sys
import numpy as np
import cv2
from PIL import Image
from collections import defaultdict

from collections import Counter
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction import DictVectorizer
from sklearn.metrics import classification_report

from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix
from sklearn.base import TransformerMixin
import numpy as np
import random

import nltk
from nltk.corpus import stopwords
from collections import defaultdict


class Featurizer(TransformerMixin):
    """Our own featurizer: extract features from each document for DictVectorizer"""

    PREFIX_WORD_NGRAM="W:"
    PREFIX_CHAR_NGRAM="C:"
    
    def fit(self, x, y=None):
        return self
    
    def transform(self, X):
        """
        here we could add more features!
        """
        out= [self._word_ngrams(text,ngram=self.word_ngrams)
                for text in X]
        return out

    def __init__(self,word_ngrams="1",binary=True,lowercase=False,remove_stopwords=False):
        """
        binary: whether to use 1/0 values or counts
        lowercase: convert text to lowercase
        remove_stopwords: True/False
        """
        self.DELIM=" "
        self.data = [] # will hold data (list of dictionaries, one for every instance)
        self.lowercase=lowercase
        self.binary=binary
        self.remove_stopwords = remove_stopwords
        self.stopwords = stopwords.words('dutch')
        self.word_ngrams=word_ngrams

        
    def _word_ngrams(self,text,ngram="1-2-3"):

        d={} #dictionary that holds features for current instance
        if self.lowercase:
            text = text.lower()
        words=text.split(self.DELIM)
        if self.remove_stopwords:
            words = [w for w in words if w not in self.stopwords]

        for n in ngram.split("-"):
            for gram in nltk.ngrams(words, int(n)):
                gram = self.PREFIX_WORD_NGRAM + " ".join(gram)
                if self.binary:
                     d[gram] = 1 #binary
                else:
                    d[gram] += 1
        return d

def show_most_informative_features(vectorizer, classifier, n=20): # a function that returns the most informative features
    feature_names = vectorizer.get_feature_names()
    for i in range(0,len(classifier.coef_)):
        coefs_with_fns = sorted(zip(classifier.coef_[i], feature_names))
        top = zip(coefs_with_fns[:n], coefs_with_fns[:-(n + 1):-1])
        print("i",i)
        for (coef_1, fn_1), (coef_2, fn_2) in top:
            print("\t%.4f\t%-15s\t\t%.4f\t%-15s" % (coef_1, fn_1, coef_2, fn_2))

def load_tweets_labels():
	
	positive_sentences = open('positivity_tweets.txt').readlines() #open the text file with the positive tweets
	negative_sentences = open('negativity_tweets.txt').readlines() #open the text file with the negative tweets
	
	positive_labels = ["Positive" for sentence in positive_sentences] #assign labels to both positive and negative tweets
	negative_labels = ["Negative" for sentence in negative_sentences]
    
	sentences = np.concatenate([positive_sentences,negative_sentences], axis=0)
	labels = np.concatenate([positive_labels,negative_labels],axis=0)

	assert(len(sentences) == len(labels))
	data = list(zip(sentences, labels))  #create one dataset with the tweets and their corresponding label
	
	random.shuffle(data) #randomize the order of the dataset
	
	return data
	
def main(argv):
	
	random.seed(113)
	print('Loading data....')
	data = load_tweets_labels() #load tweets and labels
	
	print('Splitting data....')
	split_point = int(0.80 * len(data)) #create split point for the data
	split_point2 = int(0.90 * len(data))
	
	print('Tagging data....') #tag the data 
	sentences = [sentence for sentence, label in data]
	labels = [label for sentence, label in data]
	
	
	#create X_train, X_test, X_dev, Y_train, Y_test and Y_dev sets by splitting the tweets and labels by using the split point
	# train, test, dev contains respectively 80%, 10% and 10 % of the complete dataset
	
	X_train, X_test, X_dev = sentences[:split_point], sentences[split_point:split_point2], sentences[split_point2:]
	y_train, y_test, y_dev = labels[:split_point], labels[split_point:split_point2], labels[split_point2:]
	
	assert(len(X_train)==len(y_train))
	assert(len(X_test)==len(y_test))
	
	print('Vectorize data....')
	
	#assign features to every tweet by using the predefined featurizer 
	featurizer = Featurizer(word_ngrams="1-2")
	#vectorize the features with the Dictvectorizer() function from sklearn
	vectorizer = DictVectorizer()
	
	# extract the features from each tweet as dictionaries
	X_train_dict = featurizer.fit_transform(X_train)
	X_test_dict = featurizer.transform(X_test)
	'''X_dev_dict = featurizer.transform(X_dev)'''
	
	# then convert them to the internal representation (maps each feature to an id)
	X_train = vectorizer.fit_transform(X_train_dict)
	X_test = vectorizer.transform(X_test_dict)
	'''X_dev = vectorizer.transform(X_dev_dict)'''
	
	# determine a classifier
	classifier = LogisticRegression()
	
	# Train model and predict scores
	print("Training model..")
	classifier.fit(X_train, y_train)
	#
	print("Predict..")
	y_predicted = classifier.predict(X_test)
	
	# Evaluate the system
	print("Accuracy:", accuracy_score(y_test, y_predicted))
	print
	
	print('Classification report:')
	print(classification_report(y_test, y_predicted))
	print
	
	print('Confusion matrix:')
	print(confusion_matrix(y_test, y_predicted))
	print
	
	print('Most informative features:')
	show_most_informative_features(vectorizer, classifier, n=20)
	
if __name__ == '__main__':
	main(sys.argv)
