#coding=utf-8
from selenium import webdriver
import io
import sys

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='gb18030')  # 改变标准输出的默认编码
driver = webdriver.Chrome(executable_path=r'E:\Python\chromedriver.exe')
driver.get('http://www.santostang.com/2018/07/04/hello-world/')
# print(driver.page_source)
driver.switch_to.frame(driver.find_element_by_css_selector("iframe[title='livere']"))
print(driver.page_source)
# comment = driver.find_element_by_css_selector('div.reply-content')
# content = comment.find_element_by_tag_name('p')
# print(content.text)