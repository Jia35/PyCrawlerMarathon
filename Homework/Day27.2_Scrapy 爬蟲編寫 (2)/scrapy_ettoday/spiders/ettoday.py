import scrapy
from scrapy_ettoday.items import ScrapyEttodayItem


class EttodaySpider(scrapy.Spider):
    name = 'ettoday'
    allowed_domains = ['www.ettoday.net']
    start_urls = ['https://www.ettoday.net/news/20201112/1852684.htm', 'https://www.ettoday.net/news/20201112/1852663.htm', 'https://www.ettoday.net/news/20201109/1850538.htm']

    def parse(self, response):
        item = ScrapyEttodayItem()
        item['title'] = response.xpath('//article/div/header/h1/text()').get()
        item['content'] = response.xpath('//div[@itemprop="articleBody"]//p/text()').getall()
        yield item
