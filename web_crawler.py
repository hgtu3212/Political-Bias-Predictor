from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from scrapy.item import Item, Field

class MyItem(Item):
    url = Field()

class MySpider(CrawlSpider):
    name = 'huffpost.com'
    allowed_domains = ['huffingtonpost.com']
    start_urls = ['http://www.huffingtonpost.com/entry/andrew-cuomo-gun-control_5606e323e4b0dd850307cf4c?utm_hp_ref=politics']
    print 'hi'
    rules = (
        # Extract links matching 'category.php' (but not matching 'subsection.php')
        # and follow links from them (since no callback means follow=True by default).
        Rule(LinkExtractor(allow=('huffingtonpost.com/'), deny=('live.huffingtonpost.com/r/highlight/' )), callback='parse_item', follow =True))
    print 'hi2'
    def parse_item(self, response):
        print self, response
        item = MyItem()
        item['url'] = response.url
        print "done"
        return item