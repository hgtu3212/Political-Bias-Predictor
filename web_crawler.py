import newspaper
import csv

def read_list_of_links(filename):
  """
  Reads in a txt file containing links into a list
  """
  lines = []
  with open(filename) as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
      lines.append(row[0])
  return lines


def get_article_text(link):

    text = []
    newspapr = newspaper.build(link)
    for article in newspapr.articles:
      # print(article.url)
      text.append(article.text)

    return text

# print read_list_of_links("huffington_post_links.txt")
# print read_list_of_links("fox_news_links.txt")
print read_list_of_links("blaze_news_links.txt")
print get_article_text("http://foxnews.com/politics/index.html")

