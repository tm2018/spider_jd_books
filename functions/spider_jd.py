# -*- coding: UTF-8 -*-

import urllib2
import chardet
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

#计数：访问book_info的次数


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

#用selenium.webdriver模拟浏览器访问，获取相关信息
count = 1
def getBookHtml(url):
    browser = webdriver.Chrome()
    browser.get(url)
    #try...catch尝试取访问并且取值，如果遇到异常则把各种值设置为0并输入url
    try:
        # 让webdriver等待，直到获取到了价格
        WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.XPATH, '//strong[@id="jd-price"]')))
        book_name = browser.find_element_by_xpath('//*[@id ="name"]/div[@class="sku-name"]').text
        jd_price = browser.find_element_by_xpath('//strong[@id="jd-price"]').text
        pricing = browser.find_element_by_xpath('//*[@id="page_maprice"]').text
        publishing_house = browser.find_element_by_xpath('//*[@id="parameter2"]/li[@clstag="shangpin|keycount|product|chubanshe_3"]/a').text
    except Exception as e:
        print "this is an error when get book_info:%s" %e
        book_name = 0
        jd_price =0
        pricing = 0
        publishing_house =0
        pass
    book_info = {
            "book_name": book_name,
            "jd_price": jd_price,
            "pricing": pricing,
            "publishing_house": publishing_house
    }
    browser.quit() #模拟访问完一个就关闭掉一个

    return book_info






