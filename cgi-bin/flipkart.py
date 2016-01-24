#!C:/Python27/python
#-*-coding:utf-8-*-
from os import *
import cgi
from bs4 import BeautifulSoup
import urllib2
import json
import re

class Flipkart():
    def main(self):
        fs = cgi.FieldStorage()
        names = []
        links = []
        prices = []
        srcs = []
        data = []
        items = set()
        page = urllib2.urlopen('http://www.flipkart.com/search?q='+fs["keyword"].value)
        soup = BeautifulSoup(page)
        pat = re.compile(r'href="([^"]*)"')
        for i in soup.findAll(attrs={"data-lazyload" : re.compile(".*")}):
            srcs.append(i["data-lazyload"])
        for i in soup.find_all("div", class_="p-name"):
            names.append(i.get_text().strip())
        for i in soup.find_all(href=re.compile("item.*html$"), target="_blank"):
            h = pat.search(str(i))
            href = h.group(1)
            items.add(href)
        for i in items:
            links.append(i)
            url_id = i.split('/')[-1].split('.')[0]
            f = urllib2.urlopen(''+url_id, timeout=5)
            price = json.loads(f.read())
            f.close()
            prices.append(price[0]['p'])
        data.append(names)
        data.append(links)
        data.append(prices)
        data.append(srcs)
        print "Content-type: application/json\n"
        print json.dumps(data)
flipkart = Flipkart()
flipkart.main()
