#!C:\Python27\python.exe
# -*- coding: UTF-8 -*-
 
print
#引入模块
import urllib
import urllib2
import re
import MySQLdb

#定义类
class News:

    #init
    def __init__(self):
        self.url="http://news.baidu.com/"


    #getpage
    def getpage(self):
        url=self.url
        request=urllib2.Request(url)
        response=urllib2.urlopen(request)
        return response.read()
    

    #gettitle
    def gettitle(self):
        page=self.getpage()
        #print content 
        left=re.compile('<div id="headline-tabs" class="mod-headline-tab">(.*?)<ul id="goTop" class="mod-sidebar">',re.S)
        pattern=re.search(left,page)
        return pattern.group(1)           
    def geta(self):
        page=self.gettitle()
        #print content 
        left=re.compile('<a href="(http://.*?").*?">(.*?)</a>',re.S)
        pattern=re.findall(left,page)
        return pattern
    def toimg(self,data):
        res=re.compile('<img .*?>')
        con=re.sub(res,'',data)
        return con






db= MySQLdb.connect("localhost","root","root","python",charset="gbk")
cursor = db.cursor()
new=News()
arr= new.geta()
for i in range(len(arr)):
    for item in arr:
        print item[0][:-1],new.toimg(item[1])
        sql = "INSERT INTO two(title,url) VALUES (%s, %s)" %("'"+new.toimg(item[1])+"'","'"+item[0][:-1]+"'")
        #print sql
        try:
            cursor.execute(sql)
            db.commit()
        except:
            # Rollback in case there is any error
            db.rollback()
