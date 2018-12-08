#coding:utf-8
###这个文件是对二级分类下书籍信息进行处理，获取我们需要的数据
from get_book_nav_info import getBookNav
from spider_jd import getNav2HtmlFun
from lxml import etree
import re

#处理下获取到的url_str字符串，返回最终访问京东的合适的url
def combine_url(url_str):
    pattern = re.compile("\d+-\d+-\d+")
    cat_resoure = pattern.findall(url_str)[0]
    cat_list = cat_resoure.split("-")
    cat = ",".join(cat_list)
    tid = cat_list[-1]
    url = "%s?cat=%s&tid=%s" %('https://list.jd.com/list.html',cat,tid)
    return url

b = getBookNav()
for i in b:
        for k in i:
                # print k,i[k]
                urls = map(combine_url,i[k])
                print urls

a = getNav2HtmlFun('https://list.jd.com/list.html?cat=1713,3285,3760&tid=3760')
# print a

def get_nav2_book_info(html):
        tree = etree.HTML(html)
        next_page = tree.xpath("//*[@id='J_bottomPage']/span[1]/a[10]/@href")
        # if next_page:

        # books_url = tree.xpath("//*[@id='plist']/ul/li/div/div[3]/a/@href")
        # for book_url in books_url:
        #         xpath_pattern = "//*[@id='plist']/ul/li/div/div[3]/a[@href='%s']/em/text()" %book_url
        #         book_name = tree.xpath(xpath_pattern)
        #         print book_name[0],book_url
get_nav2_book_info(a)
# combine_url(url_str)




