import pandas as pd
import scrapy
import string

from kyphrase.items import Word

URL = "https://knowyourphrase.com/{index}"
indexlist = list(string.ascii_lowercase)[:-6]
indexlist += ['uv', 'w', 'xyz']

class KyphraseSpider(scrapy.Spider):
    name = "kyphrase"

    def __init__(self):
        self.start_urls = [URL.format(index=index) for index in indexlist]

    def parse(self, response):
        dic = {}
        category = response.url.split("/")[-1]
        phrases = response.css("u::text").getall()
        if len(phrases)==0:  # the url ended with "n" has no <u> tag.
            phrases = response.css("a::text").getall()[27:-1]
        else:
            i = 0
            while i < len(phrases):
                if phrases[i][0].isupper():
                    break
                i += 1
            phrases = phrases[i:]

        dic['phrases'] = phrases
        num_ph = len(dic['phrases'])

        meanings = response.css("p::text").getall()
        dic = self.valid_meanings(dic, meanings, num_ph)

        hrefs = response.css('a[href*=knowyourphrase]::attr(href)').getall()
        dic = self.valid_hrefs(dic, phrases, hrefs, num_ph)

        df = pd.DataFrame(dic)
        df.style.format({"href":self.add_hyper})

        for i, each in df.iterrows():
            word = Word(phrase=each["phrases"], definition=each["meaning"], url=each["href"])
            yield word

    def valid_hrefs(self, dic, phrases, hrefs, len_phrases):
        phrase = phrases[0].lower()
        for letter in phrase[:5]:
            if letter in string.punctuation or letter == '’':
                phrase = phrase[:5].replace(letter,"")
        detail = "-".join(phrase[:5].split())

        for j in range(len(hrefs)):
            if detail in hrefs[j]:
                break

        dic['href'] = hrefs[j:j+len_phrases]
        return dic

    def valid_meanings(self, dic, meanings, len_phrases):
        try:
            for i in range(len(meanings)):
                if meanings[i].startswith("‘ "):
                    startindex = i+1
                if meanings[i].startswith(" – "):
                    meanings.pop(i)
                    i -= 1
        except:
            pass

        dic['meaning'] = meanings[startindex:startindex+len_phrases]
        return dic

    def add_hyper(self, val):
        url = f"https://custom.url/{val}"
        return f'=HYPERLINK({url}, {val})'