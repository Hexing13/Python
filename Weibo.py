# -*- coding:UTF-8 -*-
import cookielib
import re
import urllib
import urllib2
import time

__author__ = 'hexing'
#用户代理
heads = {'User-Agent':'Mozilla/5.0 (X11; Linux i686 (x86_64)) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.125 Safari/537.36'}

# 初始化一个CookieJar来处理Cookie
cookieJar = cookielib.CookieJar()
# 实例化一个全局opener
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookieJar))
# 把这个cookie处理机制装上去,大概是这个意思-.-
urllib2.install_opener(opener)

#获取网页源码
def getHtml(url,data=None,headers=heads):
    request = urllib2.Request(url=url,data=data,headers=headers)
    return urllib2.urlopen(request).read()

#获取微博登录界面的源码
url = 'http://login.weibo.cn/login/?ns=1&revalid=2&backURL=http%3A%2F%2Fweibo.cn%2F&backTitle=%CE%A2%B2%A9&vt='
html = getHtml(url)
print html

#由界面源码获取'vk'的值
m = re.search(r'name="vk"\s+value="(.*?)"',html)
vk = m.group(1)
pa = vk[0:4]

# print 'password_'+pa,vk
#登录微博所需提交的数据
postdate = urllib.urlencode({
    'mobile':'18829291825',
    'password_'+pa:'hx106107',
    'remember':'on',
    'backURL':'http%3A%2F%2Fweibo.cn%2F',
    'backTitle':'微博',
    'tryCount':'',
    'vk':vk,
    'submit':'登录'
})

url1='http://login.weibo.cn/login/?rand=1136703992&backURL=http%3A%2F%2Fweibo.cn%2F&backTitle=%E5%BE%AE%E5%8D%9A&vt=4&revalid=2&ns=1'
html1 = getHtml(url1,postdate)
print html1
