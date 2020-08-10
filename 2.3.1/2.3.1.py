#/user/bin/python
#coding: utf-8
import requests  # 引入包requests

link = "http://www.santostang.com/"  # 定义link为目标网页地址

headers = {'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'}

r = requests.get(link, headers=headers)  # 请求网页
print(r.text)  # r.text是获取的网页内容代码
