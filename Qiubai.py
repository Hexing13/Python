# -*- coding:UTF-8 -*-
import re
import urllib2

__author__ = 'hexing'

heads = {'User-Agent':'Mozilla/5.0 (X11; Linux i686 (x86_64)) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.125 Safari/537.36'}
i = 1
#获取网页源码
def getHtml(url,data=None,headers=heads):
    request = urllib2.Request(url=url,data=data,headers=headers)
    return urllib2.urlopen(request).read()

html = getHtml('http://www.qiushibaike.com/hot/page/1')
pattern = re.compile('<div.*?author">.*?<a.*?<img.*?>(.*?)</a>.*?<div.*?'+
                         'content">(.*?)<!--(.*?)-->.*?</div>(.*?)<div class="stats.*?class="number">(.*?)</i>',re.S)
items = re.findall(pattern,html)
for item in items:
    haveImg = re.search("img",item[3])
    if not haveImg:
        i = i+1
        print '第%s个：'%i
        print '作者：',item[0]
        print '内容：',item[1]
        print '发布时间：',item[2]
        print '点赞数：',item[4]
