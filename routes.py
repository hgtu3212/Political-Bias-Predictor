from flask import Flask, render_template, request, abort, jsonify
# from flask.ext.sqlalchemy import SQLAlchemyapp
import pickle
import gzip
from sklearn import linear_model
import numpy as np
import articleparser
import readability
import urllib
import lxml
from bs4 import BeautifulSoup
from forms import textInputFromForm	

app  = Flask(__name__)

def get_freq_map(string):
	"""
	Given a string of words, calculates the frequency (as a decimal)
	of occurrences of each word in the sentence
	"""
	freq_dict = {}
	word_list = string_to_word_list(string)
	for word in word_list:
		if word in freq_dict.keys():
			freq_dict[word] += 1.0 / len(word_list)
		else:
			freq_dict[word] = 1.0 / len(word_list)
	return freq_dict


def create_article_vector(all_words, freq_map):
	"""
	Creates a vector out of an article's freq map to prepare data for training
	"""
	features = []
	for word in all_words:
		if word in freq_map.keys():
			features.append(freq_map[word])
		else:
			features.append(0)
	return np.array(features)

def predict(model, left, right, new):
	"""
	Estimate the slant of each article in new based on left and right training examples.
	"""
	# Predict on new data
	all_words = get_all_words(left + right)
	prediction_matrix = create_prediction_matrix(all_words, new)
	prediction_list = []
	for i in range(len(prediction_matrix)):
		row_to_predict = prediction_matrix[i]
		prediction = round(model.predict(row_to_predict) + 3.18, 2)
		prediction_list.append(prediction)

	return np.array(prediction_list)

def getObjFromPklz(infilename):
	"""
	get an object file
	"""
	f = gzip.open(infilename, 'rb')
	try:
	    return pickle.load(f)
	finally:
	    f.close()
# (big_data_full, big_words_full, big_tags_full) = getObjFromPklz('read_training.txt')

def writeToPklz(outfilename, obj):
	"""
	Store an object as a file
	"""
	output = gzip.open(outfilename, 'wb')
	try:
		pickle.dump(obj, output, -1)
	finally:
		output.close()

# @app.route('http://biashtx.azurewebsites.net/')
@app.route('/', methods = ['GET', 'POST']) 
def home():
	
	form = textInputFromForm(request.form)
	if request.method == 'POST':
		print 'here'
		print request.form['textinput']
		data = {
		'input' : request.form['textinput']
		}# format the records you received into list of dictionaries
		rating = handle_get_vector(data['input'])
		params = {'rating' : rating}
		return render_template('success.html', params = params)
	return render_template('index.html', form=form)

def parse_input(input_string):
	"""
	parse input as string or as url
	"""
	if input_string[0:4] == 'http':
		return articleparser.parseArticles([input_string])
	else:
		return input_string


@app.route('/get_vector')
def handle_get_vector(stringInput):

	#parse the input into text if url
	textInput = parse_input(stringInput)
	#Get vector with our given input data 
	model = getObjFromPklz("first_clf")
	#run our input through our model
	vect = {'rating': predict(model[0],model[1],model[2], textInput)}
	# return dictionary
	return vect['rating'][0]

def get_all_words(articles):
	"""
	Returns a sorted list of all words from all articles inputted
	"""
	word_list = []
	for article in articles:
		word_list += string_to_word_list(article)
	word_list = list(set(word_list))
	return sorted(word_list, key=str)

def create_prediction_matrix(all_words, new):
	"""
	Creates the feature data matrix for the new data to be predicted on
	"""
	feature_list = []
	for article in new:
		feature_row = create_article_vector(all_words, get_freq_map(article))
		feature_list.append([1] + feature_row)
	return np.array(feature_list)

def string_to_word_list(string):
	"""
	Converts a string (title or article) into a list of string_to_word_list.
	Data processing helper function.
	"""
	word_list = []
	word = ''
	for char in string:
		if char.isalnum():
			word += char
		else:
			if word != '':
				# If the word only contains letters
				if word.isalpha():
					word_list.append(word.lower())
				# If the word contains at least 1 number
				else:
					word_list.append('xxnumberxx')
				word = ''
	if word != '':
		word_list.append(word)
	return word_list


if __name__ == '__main__':
	app.run(debug=True)