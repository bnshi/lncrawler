# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy.exceptions import DropItem
import  logging

class LncrawlerPipeline(object):
    def __init__(self)
        self.file = open('ln.txt', 'a+')


    def process_item(self, item, spider):
        self.file.write(item['table']+'\n')
        return item
