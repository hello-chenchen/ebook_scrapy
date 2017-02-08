# -*- coding: utf-8 -*-

import scrapy
import MySQLdb

conn = MySQLdb.connect(host="localhost",user="root",passwd="123456",db="book",charset="utf8")
cur = conn.cursor() 
cur.execute("SET NAMES utf8") 
cur.execute("SET CHARACTER_SET_CLIENT=utf8") 
cur.execute("SET CHARACTER_SET_RESULTS=utf8")
str_searchTable = "SELECT * FROM tb_bookname WHERE name = 'tangchaoxiaoxianren'"
cur.execute(str_searchTable)
urls = []
for row in cur.fetchall():    
    urls.append(row[1])
#conn.close

class DmozSpider(scrapy.Spider):
    name = "dmoz"
    allowed_domains = ["dmoz.org"]
    start_urls = urls

    def parse(self, response):
        items = response.xpath('/html/body/div/article/div/ul/li')
        item = items[1].xpath('a/text()').extract()
        print item[0]
        print 'chen1'
        itemlink = items[1].xpath('a/@href').extract()
        link_pos = itemlink[0].rfind('/')
        str_link = urls[0] + itemlink[0][link_pos+1:len(itemlink[0])]
        print str_link
        # str_urls = []
        # str_urls.append(str_link)
        # print str_contact
        str_insert = "INSERT INTO tb_bookchapter VALUES ('%s','tangchaoxiaoxianren','%s','')"%(item[0], str_link)
        cur.execute(str_insert)
        conn.commit()
if conn:
    conn.close

