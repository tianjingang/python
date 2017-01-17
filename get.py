#!C:\Python27\python.exe
# -*- coding: UTF-8 -*-
#引入采集模块
import urllib,urllib2
#引入正则匹配模块
import re
#要采集的地址
url='http://www.qiushibaike.com/hot/'
#防乱码标识
User='Mozilla/5.0 (Windows NT 6.3; WOW64; rv:49.0) Gecko/20100101 Firefox/49.0'
#定义header头
header={'User-Agent':User}
def reserver(url, header):
	#模拟请求
	request=urllib2.Request(url,headers=header)
	response=urllib2.urlopen(request)
	result=response.read().decode('utf-8')
	#print result
	res=re.compile('<div class="author clearfix">.*?<a href=".*?" target="_blank" title="(.*?)">
    <div class=".*?">(.*?)</div>.*?</div>',re.s)
	print res
	#f=urllib.urlopen(url)
	#print f.read()
f = reserver(url, header)


 


