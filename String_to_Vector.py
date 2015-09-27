#HackTexas Project: BiaSeek

#Raymond Cano
import nltk
from nltk.corpus import wordnet as wn
import time 

def create_bins(words, frequency_list):
	"""
	args: words is in (word.pos.number) format
	"""
	bins = []
	doneWith = set([])
	array = words.copy()
	for i in range(len(words)):
		new_bin = set([])
		main_word = frequency_list.pop(0)
		new_bin.add(main_word)
		#we're done with word, don't iterate over it anymore
		doneWith.add(words[i])
		for j in range(len(words)):
			if words[j] not in doneWith:
				if closeEnough(main_word, words[j]): #if the two words are close enough together
					new_bin.add(words[j])
					doneWith.add(words[j])
		bins.append(new_bin)
	return bins

def convertToWn(bagOfTokens):
	"""
	given a word, return the word's sense
	"""
	synsets = []
	verbSet = set(['VBD', 'VB', 'VBN', 'VBG', 'VBZ', 'VBP'])
	adjSet = set(['JJ', 'JJR', 'JJS'])
	nounSet = set(['NN', 'NNS','NNP','NNPS'])
	advSet = set(['RB', 'RBR', 'RBS'])
	tagged = tag_unigrams(bagOfWords)
	posTagged = []
	for item in tagged:
		if item[1] in adjSet:
			posTagged.append(item[0] + '.a.01')
		if item[1] in advSet:
			posTagged.append(item[0] + '.r.01')
		if item[1] in nounSet:
			posTagged.append(item[0] + '.n.01')
		if item[1] in verbSet:
			posTagged.append(item[0] + '.v.01')
	return posTagged


def parse_sentence(sentence):
	"""
	given an input article, return an array of words
	"""
	# global tokenizer
	# if not tokenizer:
	# 	init_nltk()
	tokenizer = nltk.tokenize.RegexpTokenizer(r'\w+|[^\w\s]+')
	tokens = tokenizer.tokenize(sentence)
	for item in tokens:
		if item == '.' or item == ',':
			tokens.remove(item)
	# tokens = word_tokenize(sentence)
	return tokens

def tag_unigrams(tokens):
	"""
	tag the tokens with their pos
	"""
	tagger = nltk.UnigramTagger(nltk.corpus.brown.tagged_sents())
	return tagger.tag(tokens)

def find_hyponyms(word):
	"""
	given a word in wordnet form, (word,pos,number) return the hyponym+ 
	"""
	return wn.synset(word).hyponyms()

def find_hypernyms(word):
	"""
	given a word in wordnet form, (word,pos,number) return the hyponym+
	"""
	return wn.synset(word).hypernyms()

def find_similarity(dog, cat):
	"""
	given two words find the similarity between the two
	"""
	return wn.synset(dog).wup_similarity(wn.synset(cat))




sentence = "Testing our basic parser"
sentence2 = " Stores variables, mostly regular expressions, which may be language-dependent for correct application of the algorithm. An extension of this class may modify its properties to suit a language other than English; an instance can then be passed as an argument to PunktSentenceTokenizer and PunktTrainer constructors."



this = wn.synset('win.n.01')
# print parse_sentence(sentence2)
# print find_hyponyms('politician.n.01')
start = time.time()
print this.hyponyms()
end = time.time()
print end - start 
	# find_hyponyms('politician.n.01')
# teststring = ""
# for i in range(100):
# 	teststring += sentence2
# items = tag_unigrams(parse_sentence(sentence2))
# for i in range (len(items)):
# 	print items[i][1]



