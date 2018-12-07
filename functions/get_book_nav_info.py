#coding: utf-8

import re
from open_jd import getJdBookUrlFun
"""
获取书籍一级分类名字&url、二级分类名字&url
"""

jd_book_sort_url = "https://book.jd.com/booksort.html"

book_nav_html = getJdBookUrlFun(jd_book_sort_url).decode("gbk").encode("utf-8")

def getBookNav1():
        #编写正则表达式
        pattern = re.compile(r'<dt><a href="(.*?)">(.*?)</dt><dd><em><a href="(.*?)">(.*?)</a></em>')
        # print  book_nav_html
        book_nav1_name = pattern.findall(book_nav_html)
        print book_nav1_name
        for i in book_nav1_name:
                print i[0],i[1]
getBookNav1()

