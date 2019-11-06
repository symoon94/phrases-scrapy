# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import os
import json
import pandas as pd

class UrbandictionaryPipeline(object):
    def process_item(self, item, spider):
        return item

class JsonWriterPipeline(object):

    def open_spider(self, spider):
        self.path = f'../../../output/{spider.name}/'
        self.makedirs(self.path)
        self.filename = self.path + spider.name
        self.file = open(f'{self.filename}.jl', 'w')
        self.df = pd.DataFrame(columns=['phrases', 'definition', 'url'])

    def close_spider(self, spider):
        self.file.close()
        read_file = pd.read_json (f'{self.filename}.jl', lines=True)
        read_file.to_excel (f'{self.filename}.xlsx', index = None, header=True)

    def process_item(self, item, spider):
        line = json.dumps(dict(item)) + "\n"
        self.file.write(line)
        return item

    def makedirs(self, path):
        if not os.path.exists(path):
            os.makedirs(path)