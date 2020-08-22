from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule

from crawler.items import CrawlerItem


class PageavailabilitySpider(CrawlSpider):
    handle_httpstatus_list = [400, 403, 404, 500, 502, 503, 504]
    name = 'pageavailability'
    allowed_domains = ['www.python.org']
    start_urls = ['http://www.python.org/', 'https://www.python.org/jobs/']
    custom_settings = {
        'LOG_FILE': 'logs/pageavailability.log',
        'LOG_LEVEL': 'INFO'
    }

    rules = (
        Rule(
            LinkExtractor(allow=(), restrict_css=('.list-recent-jobs'),),
            callback='parse_item',
            follow=True,
        ),
    )

    def parse_item(self, response):
        print('Extracting… ' + response.url)