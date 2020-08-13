# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class BlogspiderPipeline(object):
    # ������Ҫ����ĵ�ַ
    file_path = "result.txt"

    def __init__(self):
        self.article = open(self.file_path, "a+", encoding="utf-8")

    # ����ܵ��Ĵ�����
    def process_item(self, item, spider):
        title = item["title"]
        link = item["link"]
        content = item["content"]
        output = title + '\t' + link + '\t' + content + '\n\n'
        self.article.write(output)
        return item
