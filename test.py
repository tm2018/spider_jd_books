#coding:utf-8
import re
str = "//list.jd.com/1713-4855-4881.html"
def combine_url(str):
    pattern = re.compile("\d+-\d+-\d+")
    cat_resoure = pattern.findall(str)[0]
    cat_list = cat_resoure.split("-")
    cat = ",".join(cat_list)
    tid = cat_list[-1]
    return {"cat":cat,"tid":tid}

print combine_url(str)