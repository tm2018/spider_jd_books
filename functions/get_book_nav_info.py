#coding: utf-8

import re
from lxml import etree
from open_jd import getJdBookUrlFun
"""
获取书籍一级分类名字&url、二级分类名字&url
"""

jd_book_sort_url = "https://book.jd.com/booksort.html"

book_nav_html = getJdBookUrlFun(jd_book_sort_url).decode("gbk").encode("utf-8")

def getBookNav1():
        # print  book_nav_html
        #正则表达式，本程序用xpath
        # pattern = re.compile(r'<dt><a href="(.*?)">(.*?)</a><b></b></dt>' r'<dd><em><a href="(.*?)">(.*?)</a></em></dd>')
        # book_nav1_name = pattern.findall(book_nav_html)

        selector = etree.HTML(book_nav_html)
        content = selector.xpath('//*[@id="booksort"]/div[2]/dl/dt/text()')
        print content

        # # print book_nav1_name
        # for i in book_nav1_name:
        #         print("正则---")
        #         print i[0],i[1]
getBookNav1()

