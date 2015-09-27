import newspaper
import readability
import urllib
import lxml
from bs4 import BeautifulSoup

### Uses newspaper, readability, urllib, lxml, and BeautifulSoup python libraries to parse newspaper text ###

# [("cnn", "http://www.cnn.com/politics"), ("nytimes", "http://www.nytimes.com/politics"),
#               ("new yorker", "http://www.newyorker.com/news"), ("fox news", "http://www.foxnews.com/politics/index.html"),
#               ("breitbart", "http://www.breitbart.com/big-government/"), ("huffington post", "http://www.huffingtonpost.com/politics/"),
#               ("cnbc", "http://www.cnbc.com/politics/"), ("the blaze", "http://www.theblaze.com/stories/")]

<<<<<<< HEAD
print get_links()
=======
def get_links(link):

    links = []
    newspapr = newspaper.build(link)
    for article in newspapr.articles:
        links.append(article.url)
>>>>>>> 465752ef876570b881b8afe4d65bf7e4f5814967

    return links

def get_article_text(links):
    '''
    
    '''
    list_articles = []
    for link in links:
        # clean up html, getting rid of unwanted text
        html1 = urllib.urlopen(link).read()
        readable_title = readability.Document(html1).short_title()
        readable_article = readability.Document(html1).summary()

        # parse html
        article_soupify = BeautifulSoup(readable_article, "lxml")
        list_articles.append(readable_title + " " + article_soupify.get_text())

    return list_articles


links1 = get_links("http://www.nytimes.com/politics")
print get_article_text(links1)



