# Scrapy Phrases and Make Them Yours

<p align="center"><img width="50%" src="https://github.com/symoon94/phrases-scrapy/blob/master/img/toy-story-woody-buzz-meme-slang-dialect-linguistic-diversity.jpg" /></p>

I'm a computer science student at the University of Arizona and it's actually been only a year since I came to the states. Still struggling with English but feel like I actually enjoy learning the foreign language! As far as I'm concerned, using __verbal phrases__ with a brilliant command is the most important key to communicate persuasively any time anywhere. It is true that I'm exposed to the foreign environment so improving my speech bit by bit but I'm not going to be too pleased to stay this level. Anyway, I made this repository just for memorizing vocabularies even in the middle of the road 😁 Jajaja. All the files here are simply just for the format and have no special things (but might seem like a pretty dirty in a way I used selectors because I'm not even much familiar with the world of web) so that beginners can modify them easily (hopefully..). For memorizing words even outside, you may import an excel file into an app such as Lexilize what I'm going to use. _Yea, I totally forgot there are a bunch of useful vocabulary apps that's why I coded crawlers. However, I'm pretty sure my own words crawler can give me power not to give up easily._
<p align="center"><img width="30%" src="https://github.com/symoon94/phrases-scrapy/blob/master/img/namjoon2noogoo.png" /></p>
<p align="center">* A Screenshot of Lexilize.</p>

## Four Crawlers
1. [kyphrase.py](https://github.com/symoon94/phrases-scrapy/blob/master/kyphrase/kyphrase/spiders/kyphrase.py) [(ENG) Idiom](https://knowyourphrase.com/)  # the use of the item pipeline.
2. [inlingua.py](https://www.inlingua-edinburgh.co.uk/200-common-phrasal-verbs-with-meanings-and-example-sentences/) - [(ENG) 200-common-phrasal-verbs]("https://www.inlingua-edinburgh.co.uk/200-common-phrasal-verbs-with-meanings-and-example-sentences/")  # the simplest crawler-1.
3. [urbandictionary.py](https://github.com/symoon94/phrases-scrapy/blob/master/urbandictionary/urbandictionary/spiders/urbandictionary.py) - [(ENG) Slang](https://www.urbandictionary.com/)  # the multiple subpages crawler.
4. [spanish.py](https://github.com/symoon94/phrases-scrapy/blob/master/spanish/spanish/spiders/spanish.py) - [(SPN) 1000-most-common-spanish-words]("https://1000mostcommonwords.com/1000-most-common-spanish-words/")  # the simplest crawler-2.


## Example

### Usage
To scrape the site and save the data:

    $ cd kyphrase
    $ scrapy crawl kyphrase

### Tutorial
1. Choose a website you want to crawl! If you want to check out the allowance for the access, append '_robots.txt_' at the end of the domain.

        ex) [https://knowyourphrase.com/robots.txt](https://knowyourphrase.com/robots.txt)

2. To start scrapy:

        $ scrapy startproject kyphrase

3. Make your spider file (e.g., kyphrase.py) under the _spiders_ directory.

        ├── kyphrase
        │   ├── __init__.py
        │   ├── __pycache__
        │   ├── items.py
        │   ├── middlewares.py
        │   ├── pipelines.py
        │   ├── settings.py
        │   └── spiders
        │       ├── __init__.py
        │       ├── __pycache__
        │       └── kyphrase.py
        └── scrapy.cfg

4. Copy the code below into the spider file (e.g., kyphrase.py) and change _URL_, _indexlist_, the _class_ name, and _name_ under the class to fit your website where you want to crawl.

``` py
import scrapy

URL = "https://[YOUR_DOMAIN]/{index}"
indexlist = ["hello world", 1, 2, 3]

class KyphraseSpider(scrapy.Spider):
        name = "kyphrase"
        start_urls = [URL.format(index=index) for index in indexlist]

        def parse(self, response):
        """implement parsing here"""

        import ipdb; ipdb.set_trace() # recommend use the ipdb, an IPython debugger, but not required
```

    * To install the IPython debugger(ipdb):

            $ pip install ipdb

5. Figure out what html tags are surrounding the information what you want to extract. To view the source of the web page, append _view-source:_ at the beginning of the url. In my case:

        view-source:https://knowyourphrase.com/a

6. Code the parsing part using the debugger or a web developer tool. To note about selectors, items, and pipelines, please refer to the link below.

    - [Selectors](https://docs.scrapy.org/en/latest/topics/selectors.html)
    - [Items](https://docs.scrapy.org/en/latest/topics/items.html)
    - [Item Pipeline](https://docs.scrapy.org/en/latest/topics/item-pipeline.html)

### Error Handling
1. AttributeError: 'TelnetConsole' object has no attribute 'port'

- add a line "_TELNETCONSOLE_PORT = None_" into the settings.py or comment off this:

        EXTENSIONS = {
        'scrapy.extensions.telnet.TelnetConsole': None,
        }

2. If your crawler is blocked, you should check the allowance by appending _robots.txt_ at the end of the domain and modify settings.py.

## Author

Sooyoung Moon / [@symoon94](https://www.facebook.com/msy0128)