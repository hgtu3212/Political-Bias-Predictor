from flask import Flask, render_template, request, abort, jsonify
from flask.ext.sqlalchemy import SQLAlchemyapp = Flask(__name__)
import pickle
import gzip
from sklearn import linear_model
import numpy as np

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

@app.route('http://biashktx.azurewebsites.net/')
def home():
	return

def parse_input(input_string):
	"""
	parse input as string or as url
	"""
	

@app.route('/get_data')
def handle_data():

	#Receive data from site 

	data = {
	'input' : request.form['input']
	}# format the records you received into list of dictionaries
	model = getObjFromPklz("clf_model")
	#run our input through our model
	vect = predict(model[0],model[1],model[2], data['input'])

	# return the list of dictionaries as json
	return jsonify(rating=vect[0])