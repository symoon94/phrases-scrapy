import os
import scrapy
import pandas as pd

URL = "https://1000mostcommonwords.com/1000-most-common-spanish-words/"

class SpanishSpider(scrapy.Spider):
    name = "spanish"

    def __init__(self):
        self.start_urls = [URL]
        self.path = '../output/spanish/'
        self.makedirs()
        self.filename = self.path + "spanish.xlsx"
        self.dic = {}

    def parse(self, response):
        self.dic["Spanish"]=[]
        self.dic["English"]=[]
        result = response.css("td::text").getall()
        for i in range(0,len(result),3):
            self.dic["Spanish"].append(result[i+1])
            self.dic["English"].append(result[i+2])

        df = pd.DataFrame(self.dic)
        df.to_excel(self.filename, index=None, header=True)

    def makedirs(self):
        if not os.path.exists(self.path):
            os.makedirs(self.path)
