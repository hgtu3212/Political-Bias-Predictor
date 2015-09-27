#!/usr/bin/env python
 #-*- coding: utf-8 -*-
#POS Analysis and vectorization for a given source

#Raymond Cano

import nltk
from nltk.corpus import wordnet as wn
import time 
import math

a = nltk.corpus.brown.words()[0:10]
print a
c = "The purpose of this club is to provide an opportunity for Rice students to engage in and learn about Hip Hop culture. The club aims to form a community of Hip Hop fans, organize events, and provide educational opportunities to further enhance and improve a student’s Hip Hop knowledge and experience through music, dance, and other art forms. The Rice Hip Hop club ultimately serves Rice University’s goal to go beyond the hedges and transcend the Rice bubble."
b = "testing the tokenizer to see if it works. What happens when we put it in a sentence?"

# text = nltk.Text(word.lower() for word in nltk.corpus.brown.words())
# print text
# print text.similar('heart')
def find_similars(words, sentence):
	# sents = nltk.sent_tokenize(article)
	allwords = []
	bins = []
	tokens = nltk.word_tokenize(sentence)
	for i in range(len(words)):
		newbin = set([])
		print tokens
		text = nltk.Text(a.lower() for a in tokens)
		if i == 0:
			print text 
		text.similar(words[i])

		print 
		if similars is not None:
			for item in similars:
				newbin.add(item)
			newbin.add(words[i]) #add original word
			bins.append(newbin) #add bin to our list of bins
	return bins

print find_similars(['goal'], c)


	 


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

def tag_unigrams(tokens):
	"""
	tag the tokens with their pos
	"""
	tagger = nltk.UnigramTagger(nltk.corpus.brown.tagged_sents())
	return tagger.tag(tokens)

sent = "The latest Fox News poll asks about these issues, as well as the secretly-shot videos that show Planned Parenthood employees talking about dollar amounts associated with fetal tissue and organs from abortions." 

print parse_sentence(sent)
# print tag_unigrams(parse_sentence(sent))