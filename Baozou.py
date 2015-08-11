# -*- coding:UTF-8 -*-
import re
import urllib

#获得页面源码
def getHtml(url):
    page = urllib.urlopen(url)
    html = page.read()
    return html

#正则得到页面中想要的地址
def getImg(html):
   reg = r'http://wallpaper\.baozou\.com/s/.+\.jpg-small3'
   imgre = re.compile(reg)
   imglist = imgre.findall(html)
   x = 0
   for imgurl in imglist:
       urllib.urlretrieve(imgurl,'/home/hexing/baozou/%s.jpg'%x)
       x = x+1
   return imglist


html = getHtml("http://baozoumanhua.com/wall_papers?zg_event=%E5%A3%81%E7%BA%B8")
getImg(html)
