# -*- coding: utf-8 -*-

import scrapy
import MySQLdb

conn = MySQLdb.connect(host="localhost",user="root",passwd="123456",db="book",charset="utf8")
cur = conn.cursor() 
cur.execute("SET NAMES utf8") 
cur.execute("SET CHARACTER_SET_CLIENT=utf8") 
cur.execute("SET CHARACTER_SET_RESULTS=utf8")
str_searchTable = "SELECT * FROM tb_bookname"
cur.execute(str_searchTable)
urls = []
direcList = []
for row in cur.fetchall():    
    urls.append(row[1])
    direcList.append((row[0],row[1]))

class BookNewChapterSpider(scrapy.Spider):
    name = "bookNewChapter"
    allowed_domains = ["boquge.com"]
    start_urls = urls

    def parse(self, response):
        # print 'chen1'
        # print direcList
        # print urls
        # for direc in direcList:
        # print response.url
        # # #print direc
        # print 'chen2'
        str_name = ''
        str_linkTemp = ''
        for direc in direcList:
            if direc[1] == response.url:
                str_name = direc[0]
                str_linkTemp = direc[1]
        print response.url
        items = response.xpath('/html/body/div/article/div/ul/li')
        print items
        #print items[1]
        item = items[1].xpath('a/text()').extract()
        print item[0]
        itemlink = items[1].xpath('a/@href').extract()
        print itemlink
        link_pos = itemlink[0].rfind('/')
        str_link = str_linkTemp + itemlink[0][link_pos+1:len(itemlink[0])]
        str_insert = "INSERT INTO tb_bookchapter VALUES ('%s','%s','%s','')"%(item[0], str_name, str_link)
        print str_insert
        cur.execute(str_insert)
        conn.commit()
if conn:
    conn.close

