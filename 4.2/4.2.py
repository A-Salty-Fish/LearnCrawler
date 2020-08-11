# coding: utf-8
import requests
import io
import sys

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='gb18030')  # 改变标准输出的默认编码
link = """https://api-zero.livere.com/v1/comments/list?
callback=jQuery112407598525107806002_1597133606987
&limit=10&repSeq=4272904
&requestPath=%2Fv1%2Fcomments%2Flist
&consumerSeq=1020
&livereSeq=28583
&smartloginSeq=5154
&code=&_=1597133606989"""

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36'}

r = requests.get(link, headers=headers)
# print(r.text)

import json

json_string = r.text
# json_string = json_string[json_string.find('{')-2]
# print(json_string)
json_data = json.loads(json_string)
comment_list = json_data['results']['parents']

for eachone in comment_list:
    message = eachone['content']
    print(message)