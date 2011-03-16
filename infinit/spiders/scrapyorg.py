import re
import time
import random

from scrapy import log
from scrapy.http import Request
from scrapy.selector import HtmlXPathSelector
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.contrib.spiders import CrawlSpider, Rule
from infinit.items import InfinitItem

class ScrapyorgSpider(CrawlSpider):
    name = 'scrapyorg'
    allowed_domains = ['scrapy.org']
    start_urls = ['http://www.scrapy.org/']

    rules = (
        Rule(SgmlLinkExtractor(allow=r'Items/'), callback='parse_item', follow=True),
    )

    def parse(self, response):
        yield InfinitItem()
        timeout = random.choice(range(10))
        time.sleep(timeout)
        yield Request(self.start_urls[0], dont_filter=True)

        if timeout % 2:
            self.log("timeout is odd", level=log.WARNING)
        else:
            raise Exception("timeout is even")

    def parse_item(self, response):
        hxs = HtmlXPathSelector(response)
        i = InfinitItem()
        #i['domain_id'] = hxs.select('//input[@id="sid"]/@value').extract()
        #i['name'] = hxs.select('//div[@id="name"]').extract()
        #i['description'] = hxs.select('//div[@id="description"]').extract()
        return i
