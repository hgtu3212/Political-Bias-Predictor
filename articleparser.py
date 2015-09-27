import readability
import urllib
import lxml
from bs4 import BeautifulSoup

<<<<<<< HEAD
links = ["http://www.huffingtonpost.com/entry/john-boehner-departure-congress_5605b381e4b0768126fd952e",
         "http://www.newyorker.com/news/news-desk/what-can-china-achieve-with-cap-and-trade"]
def parseArticles(listoflinks):
	"""
	input list of links, returned as list of plain txt
	"""
	text = []
	for link in links:
	    # clean up html, getting rid of unwanted text
	    html1 = urllib.urlopen(link).read()
	    readable_title = readability.Document(html1).short_title()
	    readable_article = readability.Document(html1).summary()

	    # parse html
	    article_soupify = BeautifulSoup(readable_article, "lxml")
	    text.append(readable_title + article_soupify.get_text())
	return text
=======
links = ["http://www.nbcnews.com/news/religion/pope-francis-priests-can-forgive-abortion-if-women-are-contrite-n419321"]

for link in links:
    # clean up html, getting rid of unwanted text
    html1 = urllib.urlopen(link).read()
    readable_title = readability.Document(html1).short_title()
    readable_article = readability.Document(html1).summary()

    # parse html
    article_soupify = BeautifulSoup(readable_article, "lxml")
    print readable_title + " " + article_soupify.get_text()
>>>>>>> 4b1d7cab9c1d573dfff74826ca9c93db6b7fdc1a



