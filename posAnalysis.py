#POS Analysis and vectorization for a given source

#Raymond Cano

import nltk
from nltk.corpus import wordnet as wn
import time 
import math

def parse_sentence(sentence):
	"""
	given an input article, return an array of words
	"""
	# global tokenizer
	# if not tokenizer:
	# 	init_nltk()
	tokenizer = nltk.tokenize.RegexpTokenizer(r'\w+|[^\w\s]+')
	tokens = tokenizer.tokenize(sentence)

	# tokens = word_tokenize(sentence)
	return tokens

def tag_bigrams(tokens):
	"""
	tag the tokens with their pos
	"""
	bigram_form = []
	for i in range(0,len(tokens), 2):
		bigram_form.append([tokens[i], tokens[i+1]])
	tagger = nltk.BigramTagger(nltk.corpus.brown.tagged_sents())
	return tagger.tag(tokens)

sent = "The latest Fox News poll asks about these issues, as well as the secretly-shot videos that show Planned Parenthood employees talking about dollar amounts associated with fetal tissue and organs from abortions." 

print tag_bigrams(parse_sentence(sent))