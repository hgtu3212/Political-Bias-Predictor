# -*- coding: utf-8 -*-
from sklearn import linear_model
import numpy as np

title = 'Pope Francis and Catholic schools: Building bridges'
article = 'Of all the formal titles Pope Francis possesses — Holy Father, His Holiness, Servant of the Servants of God, etc. — there’s a particularly ancient one that I think best captures what he is embodying during this trip to the United States: “Pontifex Maximus” or, in English, “The Great Bridge Builder.” By spending time at Our Lady Queen of Angels this afternoon, Pope Francis blessed and fortified one of the most important civic “bridges” we have as Catholics and Americans. Indeed, have there been any more effective institutions providing opportunity and eventually access to the American dream for newly arrived immigrant or low-income families than America’s Catholic schools? Each and every one of our nation’s Catholic schools, especially those serving the poor and the marginalized, represents a critically important bridge for students and their families. These schools are bridges from poverty to opportunity, from isolation to community, from the daily grind to the hope of eternal life. Catholic schools have long been uniquely effective in interrupting the cycle of poverty for families living on the margins. Research suggests that students who attend Catholic schools are far more likely to graduate from high school and college, and they experience a smaller achievement gap throughout their education. Graduates of these schools are more likely to vote, they are more tolerant of diverse viewpoints, they are more civically engaged, and they earn higher wages as adults. Catholic schools have been shown to foster social capital and when they close, studies have shown that neighborhoods experience higher crime and social disorder. It’s also in the very DNA of Catholic education to welcome the stranger and immigrant, to serve the marginalized, and to honor the dignity of every human being. In light of Pope Francis’ comments on how the school is a “second home” for children, I can’t help but think of the bridge these sacred places have provided for the waves of Irish, Polish, and German immigrants who came to this country in the 19th and early 20th centuries seeking a better life, and the non-European immigrant communities of the 21st century. Lastly and most importantly, Catholic schools are spaces where our students can experience themselves as children of God. These communities are places of witness to the world where we serve the poor and celebrate the awesome dignity of every human being. By creatively reimagining how they can best serve those on the outskirts, Catholic schools have continued to pass on the faith, engage the culture, and invite others to experience the person of Jesus Christ. Ever the teacher, Francis spoke to the children about Martin Luther King and his famous dream of equality. Today Francis encouraged the children of OLQA to share that audacious dream, which is really the same American Dream that has brought so many generations of immigrants to this nation. The Holy Father praised King’s witness to hope, telling the students, "It is beautiful to have dreams and to be able to fight for them." While many Catholic schools have struggled in recent years, Our Lady Queen of Angels and its fellow Partnership Schools stand as a testimony to the enduring capacity of Catholic schools to build new bridges. Like our own Notre Dame ACE Academies, the Cristo Rey network, the Jubilee Schools of Memphis and others, the Partnership Schools are creating new models of Catholic schooling that are giving children afighting chance. These schools are re-building needed bridges toward the American Dream. Following in Francis’s footsteps, we can all encourage these dreams by investing our time and energy in the creative and entrepreneurial work that inspired the Pope’s visit to Our Lady Queen of Angels. We cannot tire of celebrating the mission of our Catholic schools — especially those on the margins — which will continue to offer sturdy bridges of hope for families across America, long after the glow of this amazing papal visit has evanesced. Rev. Timothy R. Scully, C.S.C., is the founder of the University of Notre Dame’s Alliance for Catholic Education Program and the Hackett Family Director of the University’s Institute for Educational Initiatives.'

right = ['I am pro-life.', 'Everyone has the right to life.']
left = ['I am pro-choice.', 'Everyone has the right to an abortion']
new = ['choice.']


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


def get_all_words(articles):
	"""
	Returns a sorted list of all words from all articles inputted
	"""
	word_list = []
	for article in articles:
		word_list += string_to_word_list(article)
	word_list = list(set(word_list))
	return sorted(word_list, key=str)


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

def create_training_matrices(left, right):
	"""
	Creates the feature data and result matrices to be trained on
	"""
	all_words = get_all_words(left + right)
	feature_list = []
	result_list = []

	for article in right:
		feature_row = create_article_vector(all_words, get_freq_map(article))
		feature_list.append([1] + feature_row)
		result_list.append(1)

	for article in left:
		feature_row = create_article_vector(all_words, get_freq_map(article))
		feature_list.append([1] + feature_row)
		result_list.append(-1)

	feature_matrix = np.array(feature_list)
	result_matrix = np.array(result_list)
	return feature_matrix, result_matrix


def create_prediction_matrix(all_words, new):
	"""
	Creates the feature data matrix for the new data to be predicted on
	"""
	feature_list = []
	for article in new:
		feature_row = create_article_vector(all_words, get_freq_map(article))
		feature_list.append(feature_row)
	return np.array(feature_list)


def predict(left, right, new):
	"""
	Estimate the slant of each article in new based on left and right training examples.
	"""
	# Train Model
	feature_matrix, result_matrix = create_training_matrices(left, right)
	clf = linear_model.LinearRegression()
	clf.fit(feature_matrix, result_matrix)

	# Predict on new data
	all_words = get_all_words(left + right)
	prediction_matrix = create_prediction_matrix(all_words, new)
	for i in range(len(prediction_matrix)):
		row_to_predict = prediction_matrix[i]
		prediction = clf.predict(row_to_predict)
		print prediction

	return


# print create_prediction_matrix(get_all_words(left + right), new)
print predict(left, right, new)

# freq_map_right = get_freq_map(right)
# freq_map_left = get_freq_map(left)
# print "FREQ MAP RIGHT:", freq_map_right
# print "FREQ MAP LEFT:", freq_map_left
# all_words = get_all_words([right, left])
# print all_words
# print create_vector(all_words, freq_map_right)
# print freq_map_right
# print freq_map_left







