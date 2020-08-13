# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class BlogspiderPipeline(object):
    # 填入你要保存的地址
    file_path = "result.txt"

    def __init__(self):
        self.article = open(self.file_path, "a+", encoding="utf-8")

    # 定义管道的处理方法
    def process_item(self, item, spider):
        title = item["title"]
        link = item["link"]
        content = item["content"]
        output = title + '\t' + link + '\t' + content + '\n\n'
        self.article.write(output)
        return item
