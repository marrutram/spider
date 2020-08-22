from scrapy.spiders import SitemapSpider

class SitemapurlSpider(SitemapSpider):
    name = 'sitemapurl'
    sitemap_urls = ['http://www.example.com/sitemap.xml']
    custom_settings = {
        'LOG_FILE': 'logs/sitemapurl.log',
        'LOG_LEVEL': 'INFO'
    }

    def parse(self, response):
        pass