# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from jianshu.items import ArticleItem

class JsSpider(CrawlSpider):
    name = 'js'
    allowed_domains = ['jianshu.com']
    start_urls = ['https://www.jianshu.com/']

    rules = (
        Rule(LinkExtractor(allow=r'.*/p/[0-9a-z]{12}.*'), callback='parse_detail', follow=True),
    )

    def parse_detail(self, response):
         title = response.xpath("//h1[@class='title']/text()").get()
         avatar = response.xpath("//a[@class='avatar']/img/@src").get()
         author = response.xpath("//span[@class='name']/a/text()").get()
         put_time = response.xpath("//span[@class='publish-time']/text()").get().replace("*","")
         url = response.url
         url1 = url.split("?")[0]
         article_id = url1.split('/')[-1]
         content = response.xpath("//div[@class='show-content']").get()
         word_count = response.xpath("//span[@class='wordage']/text()").get()
         read_count = response.xpath("//span[@class='views-count']/text()").get()
         like_count = response.xpath("//span[@class='likes-count']/text()").get()
         comments_count = response.xpath("//span[@class='comments-count']/text()").get()
         item = ArticleItem(title=title,avatar=avatar,author=author,put_time=put_time,orgin_url = response.url,article_id=article_id,content=content,word_count=word_count,read_count=read_count,like_count=like_count,comments_count=comments_count)
         yield item



