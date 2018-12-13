# -*- coding: UTF-8 -*-

import urllib2
import chardet
# import sys
# reload(sys)
# sys.setdefaultencoding('utf-8')

#定义url
jd_book_url = "https://book.jd.com/"
jd_book_sort_url = "https://book.jd.com/booksort.html"

#定义一个函数假装访问jd主页
def getJdUrlFun(url):
        headers = {
            "user_agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36"
        }
        req = urllib2.Request(url,headers = headers)
        res_data = urllib2.urlopen(req,timeout=10)
        res = res_data.read()
        res_data.close()
        print "我在假装访问京东图书主页"
        return res

#定义一个函数访问京东图书
def getJdBookSortUrlFun(url=""):
    #假装访问京东主页
    getJdUrlFun(jd_book_url)
    headers = {
        "user_agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36",
        "referer": "https://book.jd.com/"
    }
    req = urllib2.Request(jd_book_sort_url, headers=headers)
    res_data = urllib2.urlopen(req, timeout=10)
    res = res_data.read()
    res_data.close()
    return res

#获取图书二级分类的html
def getNav2HtmlFun(url=""):
        headers = {
            "user_agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36",
            "referer": "https://book.jd.com/booksort.html"
        }
        req = urllib2.Request(url, headers=headers)
        res_data = urllib2.urlopen(req, timeout=10)
        res = res_data.read()
        res_data.close()
        return res

# print getJdBookUrlFun(jd_book_url).decode("gbk").encode("utf-8")

#获取每本图书的html，其中需要传入referer和url
def getBookHtml(url,referer):
    headers = {
        "user_agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36",
        "referer": referer
    }
    print headers
    req = urllib2.Request(url, headers=headers)

    res_data = urllib2.urlopen(req, timeout=10)

    res = res_data.read()
    # print chardet.detect(res)
    if isinstance(res,unicode):
            print "res is unicode!"
    # else:
    #         print res
    print res
    res_data.close()
    return res





