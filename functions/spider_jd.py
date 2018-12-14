# -*- coding: UTF-8 -*-

import urllib2
import chardet
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


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
def getBookHtml(url):
    # desired_capabilities = DesiredCapabilities.CHROME  # 修改页面加载策略
    # desired_capabilities["pageLoadStrategy"] = "none"  # 这个值表示只加载html，不加载动态获取的内容如js ajax等
    browser = webdriver.Chrome()
    browser.get(url)
    # browser.set_page_load_timeout(1)
    #让webdriver等待，直到获取到了价格
    WebDriverWait(browser, 1).until(EC.presence_of_element_located((By.XPATH, '//strong[@id="jd-price"]')))
    # browser.switch_to.frame(frame)
    price = browser.find_element_by_xpath('//strong[@id="jd-price"]')
    print price.text






