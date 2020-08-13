# coding: utf-8
import requests
import datetime
from bs4 import BeautifulSoup
from pymongo import MongoClient
import io
import sys

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='gb18030')  # 改变标准输出的默认编码
client = MongoClient('localhost', 27017)
db = client.blog_database
collection = db.blog

link = "http://www.santostang.com/"
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36'}
r = requests.get(link, headers=headers)

soup = BeautifulSoup(r.text, "html.parser")
title_list = soup.find_all("h1", class_="post-title")
for eachone in title_list:
    url = eachone.a['href']
    title = eachone.a.text.strip()
    post = {"url": url,
            "title": title,
            "date": datetime.datetime.utcnow()}
    collection.insert_one(post)
