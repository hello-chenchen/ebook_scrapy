# -*- coding: utf-8 -*-

import scrapy
import MySQLdb

urls = []
direcList = []

class DmozSpider(scrapy.Spider):
    name = "dmoz1"
    allowed_domains = ["dmoz.org"]
    conn = MySQLdb.connect(host="localhost",user="root",passwd="123456",db="book",charset="utf8")
    cur = conn.cursor()
    cur.execute("SET NAMES utf8")
    cur.execute("SET CHARACTER_SET_CLIENT=utf8")
    cur.execute("SET CHARACTER_SET_RESULTS=utf8")
    str_searchTable = "SELECT * FROM tb_bookchapter"
    cur.execute(str_searchTable)
    for row in cur.fetchall(): 
        #print row[3]
        if row[3] == '':
            urls.append(row[2])
            direcList.append((row[2],row[3]))
    #print urls
    conn.close
    start_urls = urls

    def parse(self, response):
        for direc in direcList:
            items = response.xpath('/html/body/article/div[@id="txtContent"]/text()').extract()
            str_content = ''
            for item in items:
                str_content = str_content + item
            #str_update = "UPDATE tb_bookchapter SET contact = '%s' WHERE link = '%s'"%(str_content,direcList[i_flag][0])
            # print 'chenchss'
            # print direc[0]
            str_update = "UPDATE tb_bookchapter SET contact = '"+str_content+"' WHERE link = '"+direc[0]+"'"
            #print str_update
            cur.execute(str_update)
            conn.commit()
        if conn:
            conn.close
#print items
        # item = items[1].xpath('/text()').extract()
        # print item[0]
        # str_link = urls[0] + itemlink[0][link_pos+1:len(itemlink[0])]
        # print str_link
        # str_insert = "INSERT INTO tb_bookchapter VALUES ('%s','%s')"%(item[0], str_link)

