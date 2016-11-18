#!C:\Python27\python.exe
# -*- coding: UTF-8 -*-

print   
import urllib
import urllib2
import re
import MySQLdb


class News:

    #init
    def __init__(self):
        self.url = "http://news.baidu.com/"

    #convert div to ''
    def tranTags(self, x):
        pattern = re.compile('<div.*?</div>')
        res = re.sub(pattern, '', x)
        return res

    #getPage
    def getPage(self):
        url = self.url
        request = urllib2.Request(url)
        response = urllib2.urlopen(request)
        return response.read()

    #get navCode
    def getNavCode(self):
        page = self.getPage()
        pattern = re.compile('(<div id="menu".*?)<i class="slogan"></i>', re.S)
        navCode = re.search(pattern, page)
        return navCode.group(1)
        
    #get nav
    def getNav(self):
        navCode = self.getNavCode()
        pattern = re.compile('<a href="(http://.*?/).*?>(.*?)</a>', re.S)
        itmes = re.findall(pattern, navCode)
        return itmes
        # for item in itmes:
        #     print item[0], self.tranTags(item[1])
            



db= MySQLdb.connect("localhost","root","root","python",charset="gbk")
cursor = db.cursor()
news = News()
arr= news.getNav()
for item in arr:
    print item[0], news.tranTags(item[1])
    sql = "INSERT INTO one(title,url) VALUES (%s, %s)" %("'"+news.tranTags(item[1])+"'","'"+item[0]+"'")
    #print sql
    try:
        cursor.execute(sql)
        db.commit()
    except:
        # Rollback in case there is any error
        db.rollback()

       
