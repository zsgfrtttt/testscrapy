# -*- coding: utf-8 -*-
import scrapy
from testscrapy.items import TestscrapyItem


# scrapy startproject myspider
# scrapy genspider baidu baidu.com
class BaiduSpider(scrapy.Spider):
    name = 'baidu'
    allowed_domains = ['www.80s.tw']
    start_urls = ['https://www.80s.tw/movie/list']

    def parse(self, response):
        url = 'https://www.80s.tw/'
        list = response.xpath('//div[@id="block3"]//ul[@class="me1 clearfix"]/li')
        for item in list:
            title = item.xpath("./a/@title").extract_first()
            link = url + item.xpath("./a/@href").extract_first()
            img = "http:" + item.xpath("./a[1]/img[1]/@src").extract_first()
            name = item.xpath("./h3[@class='h3']/a[1]/text()").extract_first().split()[0]
            score = item.xpath("./a/span[@class='poster_score']/text()").extract_first()

            movie = TestscrapyItem()
            movie['title'] = title
            movie['link'] = link
            movie['img'] = img
            movie['name'] = name
            movie['score'] = score
            print(movie)
            yield movie

        pager = response.xpath('//div[@class="pager"]/a')
        if (pager):
            for i in pager:
                p = i.xpath("./text()").extract_first()
                if (p == "下一页"):
                    next = url + i.xpath("./@href").extract_first()
                    print(next)
                    yield scrapy.Request(next, callback=self.parse)

