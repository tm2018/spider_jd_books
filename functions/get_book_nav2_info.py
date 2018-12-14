#coding:utf-8
###这个文件是对二级分类下书籍信息进行处理，获取我们需要的数据
from get_book_nav_info import getBookNav
from spider_jd import getNav2HtmlFun,getBookHtml
from lxml import etree
import re
import sys

##测试乱码
reload(sys)
sys.setdefaultencoding('utf-8')
#获得系统编码格式
type = sys.getfilesystemencoding()
#将网页以utf-8格式解析然后转换为系统默认格式



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
                # print urls

a ='https://list.jd.com/list.html?cat=1713,3285,3760&tid=3760'
# print a

#根据html取出下一页地址和提取书籍相关信息
def get_nav2_book_info(url):
        html = getNav2HtmlFun(url)
        tree = etree.HTML(html)
        next_page_list = tree.xpath('//*[@id="J_bottomPage"]/span[@class="p-num"]/a[@class="pn-next"]/@href')
        #图书信息可以点击“更多”进去查看，bookmore_url是他的url
        bookmore_url = tree.xpath('//*[@id="plist"]/ul/li/div/div[@class="p-name"]/a/@href')
        #把url组合起来
        bookmore_spider_url = "%s%s" %("https:",bookmore_url[0])
        #这里访问书籍信息时，假装从当前的url跳转过去，所以以当前url伪装成referer
        book_html = getBookHtml(bookmore_spider_url)
        print bookmore_spider_url

        book_name = tree.xpath("//*[@id='jd-price']/text()")
        print book_name
        try:
            if next_page_list[0]:
                    next_page = "%s%s" %("https://list.jd.com",next_page_list[0])
                    print "next_page is :%s" %next_page
            else:
                    print "next_page is null!"
        except Exception as e:
                    print "there is an error when get next_page!error_info:%s" %e
get_nav2_book_info('https://list.jd.com/list.html?cat=1713,3285,3760&tid=3760')





