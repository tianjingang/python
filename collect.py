#!C:\Python27\python.exe
# -*- coding: UTF-8 -*-

print   
#加载re模块
import re
#加载urllib2模块
import urllib,urllib2

#要采集的路径
url="http://news.baidu.com/"
#打开路径
response = urllib2.urlopen(url)
#读取内容
content= response.read()
#print content
#pattern = re.compile('(<div id="channel-all".*?)<div id="body" alog-alias="b"', re.S)
#nav = re.search(pattern, content)
#print nav.group(1)
#正则匹配
pattern1=re.compile('(<ul class="clearfix">.*?)<i class="slogan"></i>',re.S)
#获取首页导航超链接
nav=re.search(pattern1,content)
getCode=nav.group(1)

#采集导航超url和标题
pattern2=re.compile('<a href="(http://.*?/).*?>(.*?)</a>',re.S)
Code=re.findall(pattern2,getCode)
#拼接需要过滤的
    def delete(x):

for res in Code:
	print res[0],res[1]


