#/user/bin/python
#coding: utf-8
import requests  # 引入包requests
from bs4 import BeautifulSoup

link = "http://www.santostang.com/"  # 定义link为目标网页地址

headers = {'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'}

r = requests.get(link, headers=headers)  # 请求网页
soup = BeautifulSoup(r.text, "html.parser")
title = soup.find("h1", class_="post-title").a.text.strip()
print(title)
