# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymongo
from scrapy import signals
from scrapy.exporters import CsvItemExporter
import csv
import os
import sys
class MongoPipeline(object):

    def __init__(self):
        self.files = {}
        store_file = os.path.dirname(__file__) + '/item.csv'
        self.file = open(store_file,'wb')
        self.writer = csv.writer(self.file)


    @classmethod
    def from_crawler(cls, crawler):
        pipeline = cls()
        crawler.signals.connect(pipeline.spider_opened, signals.spider_opened)
        crawler.signals.connect(pipeline.spider_closed, signals.spider_closed)
        return pipeline

    def spider_opened(self, spider):
        file_name = open('query_items.csv', 'w+b')
        self.files[spider.name] = file_name
        # self.exporter = CsvItemExporter(file_name, encoding='utf-8-sig')
        self.exporter = CsvItemExporter(file_name, encoding='utf-8')
        self.exporter.fields_to_export = [spider.name]
        self.exporter.start_exporting()

    def spider_closed(self, spider):
        self.exporter.finish_exporting()
        file_close = self.files.pop(spider.name)
        file_close.close()
        print("now {} has run out to close".format(spider.name))



    def process_item(self, item, spider):
        #这里通过mongodb进行了一个去重的操作，每次更新插入数据之前都会进行查询，判断要插入的url_token是否已经存在，如果不存在再进行数据插入，否则放弃数据
        # self.db['user'].update({'url_token':item["url_token"]},{'$set':item},True)
        # return item

        print("running here to process item")
        print("the export item is {}".format(item))
        location = dict(eval(item['locations'])[1])['name'].encode(encoding='UTF-8')
        print("location is in {}".format(location))
        if item['gender'] == 0 and location == '上海' and item['answer_count'] > 0:
            print("target number is coming, add user_info")
            used_info = (item['name'], item['is_bind_sina'], item['headline'], item['description'], item['url_token'], item['thanked_count'], item['voteup_count'], item[''])
            
            self.writer.writerow(used_info)

        self.exporter.export_item(item)
        return item



