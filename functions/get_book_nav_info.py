#coding: utf-8

import re
from lxml import etree
from spider_jd import getJdBookSortUrlFun
"""
获取书籍一级分类名字&url、二级分类名字&url
"""

jd_book_sort_url = "https://book.jd.com/booksort.html"

book_nav_html = getJdBookSortUrlFun(jd_book_sort_url)

def getBookNav():
        # print  book_nav_html.decode("gbk").encode("utf-8")
        #正则表达式，本程序用xpath
        # pattern = re.compile(r'<dt><a href="(.*?)">(.*?)</a><b></b></dt>' r'<dd><em><a href="(.*?)">(.*?)</a></em></dd>')
        # book_nav1_name = pattern.findall(book_nav_html)
        # # print book_nav1_name
        # for i in book_nav1_name:
        #         print("正则---")
        #         print i[0],i[1]
        tree = etree.HTML(book_nav_html)
        #取出一级目录，暂时无用
        nav1 = tree.xpath("//*[@id='booksort']/div[2]/dl/dt/a/text()")
        #取出二级目录的名字
        nav2_names =  tree.xpath('//*[@id="booksort"]//dl/dd/em/a/text()')
        #根据二级目录名获取该目录的url，返回一个dict迭代器
        for nav2_name in nav2_names:
                url_pattern = '//*[@id="booksort"]//dl/dd/em/a[text()="%s"]/@href' %nav2_name
                nav2_url = tree.xpath(url_pattern)
                nav2_name_url = {
                        nav2_name:nav2_url
                }
                yield nav2_name_url
