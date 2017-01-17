#!C:\Python27\python.exe
# -*- coding: UTF-8 -*-
#引入采集模块
import urllib,urllib2
#引入正则匹配模块
import re

response = urllib2.urlopen("http://www.newsbaidu.com")
content=response.read()
pattern = re.compile('(<div id="channel-all".*?)<div id="body" alog-alias="b"', re.S)
nav = re.findall(pattern, content)
for navs in nav:
	print navs
