# -*- coding: utf-8 -*-
import scrapy

class LianjiaSpider(scrapy.Spider):
    name = "toscrape-lianjia"
    start_urls = [
        'http://bj.lianjia.com/chengjiao/pg2/',
    ]

    def parse(self, response):
        house_lis = response.css('.clinch-list li')
        for house_li in house_lis:
            link = house_li.css('.info-panel h2 a::attr("href")').extract_first().encode('utf-8')
            yield scrapy.Request(link)
        # image是一个list。在Scrapinghub中显示的时候会把image里所有的图片显示出来
        image_url = response.css('.pic-panel img::attr(src)').extract_first()
        yield {
            'link': response.url,
            'id': response.url.split('/')[-1].split('.')[0],
            'image': [image_url, image_url],
            'title': response.css('.title-box h1::text').extract_first(),
            'addr': response.css('.info-item01 a::text').extract_first(),
            'price': response.css('.love-money::text').extract_first()
        }
