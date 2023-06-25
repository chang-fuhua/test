import scrapy


class HupuNewsSpider(scrapy.Spider):
    name = "hupu_news"
    allowed_domains = ["www.hupu.com"]
    start_urls = ["https://www.hupu.com"]

    def parse(self, response):
        # 提取新闻列表中的详情页链接
        news_links = response.xpath('//div[@class="news-list"]/ul/li/a/@href').getall()

        for link in news_links:
            yield response.follow(link, callback=self.parse_news)

        # 处理翻页
        next_page = response.xpath('//a[@class="next"]/@href').get()
        if next_page:
            yield response.follow(next_page, callback=self.parse)

    def parse_news(self, response):
        # 提取新闻详情页的内容
        title = response.xpath('//h1/text()').get()
        content = response.xpath('//div[@class="artical-content-text"]/text()').get()

        yield {
            'title': title,
            'content': content
        }
