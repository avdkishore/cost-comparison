#!C:/Python27/python
#-*-coding:utf-8-*-
from os import *
import cgi
from bs4 import BeautifulSoup
import urllib2
import json
import re

class Amazon():
    def main(self):
        fs = cgi.FieldStorage()
        names = []
        links = []
        prices = []
        srcs = []
        data = []
        url = "http://www.amazon.in/s/field-keywords="+fs["keyword"].value
        page = urllib2.urlopen(url)
        soup = BeautifulSoup(page)
        for i in soup.find_all(lambda tag: tag.name == "div" and tag.get("class") == ['productTitle']):
            links.append(i.find("a")["href"].strip())
            names.append(i.get_text().strip())
        for i in soup.find_all("div", "newPrice"):
            prices.append(i.find("span").get_text().strip())
        for i in soup.find_all("img", attrs={"alt" : "image"}):
            srcs.append(i["src"])
        data.append(names)
        data.append(links)
        data.append(prices)
        data.append(srcs)
        print "Content-type: application/json\n"
        print json.dumps(data)
amazon = Amazon()
amazon.main()
