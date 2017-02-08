# -*- coding: utf-8 -*-

import scrapy
import MySQLdb

urls = []
direcList = []
conn = MySQLdb.connect(host="localhost",user="root",passwd="123456",db="book",charset="utf8")
cur = conn.cursor() 
cur.execute("SET NAMES utf8") 
cur.execute("SET CHARACTER_SET_CLIENT=utf8") 
cur.execute("SET CHARACTER_SET_RESULTS=utf8")
str_searchTable = "SELECT * FROM tb_bookchapter"
cur.execute(str_searchTable)
for row in cur.fetchall():
    if row[3] == '':
        urls.append(row[2])
        direcList.append((row[2],row[3]))

class BookContentSpider(scrapy.Spider):
    name = "bookContent"
    allowed_domains = ["boquge.com"]
    start_urls = urls

    def parse(self, response):
        for direc in direcList:
            items = response.xpath('/html/body/article/div[@id="txtContent"]/text()').extract()
            str_content = ''
            for item in items:
                str_content = str_content + item
            str_update = "UPDATE tb_bookchapter SET contact = '"+str_content+"' WHERE link = '"+direc[0]+"'"
            cur.execute(str_update)
            conn.commit()
if conn:
    conn.close

