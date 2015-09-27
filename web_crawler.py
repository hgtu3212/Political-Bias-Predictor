import newspaper

def get_links():
    newspapers = [("cnn", "http://www.cnn.com/politics"), ("nytimes", "http://www.nytimes.com/politics"),
              ("new yorker", "http://www.newyorker.com/news"), ("fox news", "http://www.foxnews.com/politics/index.html"),
              ("breitbart", "http://www.breitbart.com/big-government/"), ("huffington post", "http://www.huffingtonpost.com/politics/"),
              ("cnbc", "http://www.cnbc.com/politics/"), ("the blaze", "http://www.theblaze.com/stories/")]

    final_links = []
    for tupl in range(len(newspapers)):
        name = tupl[0]
        news_link = tupl[1]

        newspapr = newspaper.build(news_link)
        for article in newspapr.article:
            final_links.append((name, article.url))












