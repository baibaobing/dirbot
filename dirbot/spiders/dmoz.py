from scrapy.spiders import Spider
from scrapy.selector import Selector

from dirbot.items import Website


class DmozSpider(Spider):
    name = "dmoz"
    allowed_domains = ["dmoztools.net"]
    start_urls = [
        "http://dmoztools.net/Computers/Programming/Languages/Python/Books/",
        "http://dmoztools.net/Computers/Programming/Languages/Python/Resources/",
    ]

    def parse(self, response):
        """
        The lines below is a spider contract. For more info see:
        http://doc.scrapy.org/en/latest/topics/contracts.html

        @url http://dmoztools.net/Computers/Programming/Languages/Python/Resources/
        @scrapes name
        """
        sites = response.css('#site-list-content > div.site-item > div.title-and-desc')
        items = []

        for site in sites:
            item = Website()
            item['name'] = site.css(
                'a > div.site-title::text').extract_first().strip()
            item['url'] = site.xpath(
                'a/@href').extract_first().strip()
            item['description'] = site.css(
                'div.site-descr::text').extract_first().strip()
            items.append(item)

        return items
