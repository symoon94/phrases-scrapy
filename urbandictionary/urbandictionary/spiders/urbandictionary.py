import pandas as pd
import scrapy
import string

from urbandictionary.items import Word

URL = "https://www.urbandictionary.com/"

class UrbandictionarySpider(scrapy.Spider):
    name = "urbandictionary"

    def __init__(self):
        self.start_urls = [URL]

    def parse(self, response):
        trends_url = response.css("a.trending-link::attr(href)") \
            .getall()
        if trends_url:
            for each in trends_url:  # crawl the trend data!
                yield scrapy.Request(
                    response.urljoin(URL + each),
                    callback=self.parse)
        try:
            title = response.url.split("term=")[1].replace("%20", " ")
            if title == "":
                title = response.css("title")

            meaning = response.css('div.meaning::text').get().strip()
            if meaning == "":
                meaning = self.remove_tag(response, 'meaning')
            self.crawl_page(response, meaning)

            try:
                example = response.css('div.example').get() \
                    .split("\n")[1:-1][0]
            except:
                example = self.remove_tag(response, 'example')
            self.crawl_page(response, example)
            example=example.replace("\r","").replace("<br>"," ")

            word = Word(title=title, meaning=meaning, \
                example=example.replace("\r",""))
            yield word
        except:
            pass

    def remove_href(self, str_tags):
        if '</a>' not in str_tags:
            return ""

        if len(str_tags.split('<a href="')) > 1:
            return (str_tags.split('<a href="')[0] + str_tags.split('<a href="')[1].split('">')[1]).replace("</a>","") + self.remove_href('<a href="'.join(str_tags.split('<a href="')[2:]))

        else:
            return (str_tags.split('<a href="')[0] + str_tags.split('<a href="')[1].split('">')[1]).replace("</a>","")

    def remove_tag(self, response, category):
        str_tags = response.css(f'div.{category}').get().strip(f'<div class="{category}">').strip("</'")
        str_tags = str_tags.replace('<a class="autolink" href=',"<a href=") \
            .replace('utolink" href=',"<a href=") \
            .replace('onclick="ga(\'send\', \'event\', \'Autolink\', \'Click\',', "")
        chuncks = len(str_tags.split("&quot;"))
        new_str = ""
        for i in range(0,chuncks,2):
            new_str += str_tags.split("&quot;")[i]

        return new_str

    def crawl_page(self, response, meaning):
        if "<a href=" in meaning:
            new_url = meaning.split('<a href="')[1].split('">')[0]
            meaning = self.remove_href(meaning)
            yield scrapy.Request(
                response.urljoin(URL + new_url),
                callback=self.parse
            )