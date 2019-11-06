import os
import scrapy
import pandas as pd

URL = "https://www.inlingua-edinburgh.co.uk/200-common-phrasal-verbs-with-meanings-and-example-sentences/"

class InlinguaSpider(scrapy.Spider):
    name = "inlingua"

    def __init__(self):
        self.start_urls = [URL]
        self.path = './output/'
        self.makedirs()
        self.filename = self.path + "inlingua.xlsx"

    def parse(self, response):
        lst = []

        for each in response.css("tr"):
            row = each.css("td::text").getall()
            lst.append(row)

        df = pd.DataFrame(lst[1:], columns = lst[0])
        df.to_excel(self.filename, index=None, header=True)

    def makedirs(self):
        if not os.path.exists(self.path):
            os.makedirs(self.path)
