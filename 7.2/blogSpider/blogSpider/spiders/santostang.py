# coding: utf-8
import scrapy
from bs4 import BeautifulSoup
from blogSpider.items import BlogspiderItem
import io
import sys

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='gb18030')  # 改变标准输出的默认编码


class SantostangSpider(scrapy.Spider):
    name = 'santostang'
    allowed_domains = ['www.santostang.com']
    start_urls = ['http://www.santostang.com/']

    def parse(self, response):
        soup = BeautifulSoup(response.text, "html.parser")
        title_list = soup.find_all("h1", class_="post-title")
        for i in range(len(title_list)):
            # 将数据封装到BlogspiderItem对象，字典类型数据
            item = BlogspiderItem()
            title = title_list[i].a.text.strip()
            link = title_list[i].a["href"]
            # 变成字典
            item["title"] = title
            item["link"] = link
            # 根据文章链接，发送Request请求，并传递item参数
            yield scrapy.Request(url=link, meta={'item': item}, callback=self.parse2)

    def parse2(self, response):
        # 接收传递的item
        item = response.meta['item']
        # 解析提取文章内容
        soup = BeautifulSoup(response.text, "html.parser")
        content = soup.find("div", class_="view-content").text.strip()
        content = content.replace("\n", " ")
        item["content"] = content
        # 返回item，交给item pipeline
        yield item
