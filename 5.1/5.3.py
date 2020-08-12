# coding: utf-8
import requests
from lxml import etree

import io
import sys

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='gb18030')  # 改变标准输出的默认编码

link = "http://www.santostang.com/"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36"
}
r = requests.get(link, headers=headers)

html = etree.HTML(r.text)

title_list = html.xpath('//h1[@class="post-title"]/a/text()')
print(title_list)