import readability
import urllib
import lxml
from bs4 import BeautifulSoup

links = ["http://www.nbcnews.com/news/religion/pope-francis-priests-can-forgive-abortion-if-women-are-contrite-n419321"]

for link in links:
    # clean up html, getting rid of unwanted text
    html1 = urllib.urlopen(link).read()
    readable_title = readability.Document(html1).short_title()
    readable_article = readability.Document(html1).summary()

    # parse html
    article_soupify = BeautifulSoup(readable_article, "lxml")
    print readable_title + " " + article_soupify.get_text()



