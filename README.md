# Scrapy Phrases and Make Them Yours

## Website I tried to scrapy?
[https://knowyourphrase.com/](https://knowyourphrase.com/)

## Could I crawl this website?
Append _robots.txt_ at the end of the domain and check the allowance.
[https://knowyourphrase.com/robots.txt](https://knowyourphrase.com/robots.txt)

## Usage

    $ scrapy crawl kyphrase

## Tutorial
1. To start scrapy:

        $ scrapy startproject kyphrase

2. Make your spider file (e.g., kyphrase.py) under the _spiders_ directory.

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

3. Copy the code below into the spider file (e.g., kyphrase.py) and change _URL_, _indexlist_, the _class_ name, and _name_ under the class to fit your website where you want to crawl.

        import scrapy

        URL = "https://[YOUR_DOMAIN]/{index}"
        indexlist = ["hello world", 1, 2, 3]

        class KyphraseSpider(scrapy.Spider):
            name = "kyphrase"
            start_urls = [URL.format(index=index) for index in indexlist]

            def parse(self, response):
                """implement parsing here"""

                import ipdb; ipdb.set_trace() # recommend use the ipdb, an IPython debugger, but not required

    * To install the IPython debugger(ipdb):

            $ pip install ipdb

4. Figure out what html tags are surrounding the information what you want to extract. To view the source of the web page, append _view-source:_ at the beginning of the url. In my case:

        view-source:https://knowyourphrase.com/a

5. Code the parsing part using the debugger or a web developer tool. To note about selectors, items, and pipelines, please refer to the link below.

    - [Selectors](https://docs.scrapy.org/en/latest/topics/selectors.html)
    - [Items](https://docs.scrapy.org/en/latest/topics/items.html)
    - [Item Pipeline](https://docs.scrapy.org/en/latest/topics/item-pipeline.html)

### Error Handling
1. AttributeError: 'TelnetConsole' object has no attribute 'port'

- add a line "_TELNETCONSOLE_PORT = None_" into the settings.py or comment off this:

                EXTENSIONS = {
                'scrapy.extensions.telnet.TelnetConsole': None,
                }
