#coding: utf-8

import re
from functions.open_jd import getJdBookUrlFun

jd_book_url = "https://book.jd.com/"

print getJdBookUrlFun(jd_book_url).decode("gbk").encode("utf-8")