# -*- coding: UTF-8 -*-

import urllib2
# import sys
# reload(sys)
# sys.setdefaultencoding('utf-8')

#定义url
jd_main_url = "https://www.jd.com/"
jd_book_url = "https://book.jd.com/"

#定义一个函数假装访问jd主页
def getJdUrlFun(url):
        headers = {
            "user_agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36"
        }
        req = urllib2.Request(url,headers = headers)
        res_data = urllib2.urlopen(req,timeout=10)
        res = res_data.read()
        res_data.close()
        print "我在假装访问京东主页"
        return res

#定义一个函数访问京东图书
def getJdBookUrlFun(url):
    #假装访问京东主页
    getJdUrlFun(jd_main_url)
    headers = {
        "user_agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36",
        "referer": "https://www.jd.com/"
    }
    req = urllib2.Request(url, headers=headers)
    res_data = urllib2.urlopen(req, timeout=10)
    res = res_data.read()
    res_data.close()
    return res

# print getJdBookUrlFun(jd_book_url).decode("gbk").encode("utf-8")



