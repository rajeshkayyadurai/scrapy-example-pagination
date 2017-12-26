# Web/Data Scraping - Pagination:

This framework specializes in scraping the data from websites where pagination is incorporated.

## Framework contains the following components:

###### bases:
Maintains basic data needed with which spider works such as inputs or parameters needed to handle API request calls, selectors and URL

###### core:
Acts as the heart of the framework that comprises the whole scrapy components. Various scrapy components are spider, item, middleware, pipeline and settings

###### modules:
Contains the list of API or GUI functions required to design the spider

###### reports:
Stores the report post spider execution. Report formats viz. csv, json and xml(excel is in progress)

###### reusables:
It has collection of utility or additional functions required for web scraping

###### list.txt:
A list of rotational IPs are stored which will essentially needed when a website to be scrapped come across IP ban

###### requirements.txt:
Collection of library dependencies are maintained

###### scrapy.cfg:
An official scrapy configuration file

###### setup.py:
It will be generated either manually or automatically when the help of scrapinghub or scrapyd needed

There are two github libraries used with this framework purposely, one is to supply user agent randomly and other is to rotate IPs from its pool, to avoid IP ban.

- [scrapy-fake-useragent](https://github.com/alecxe/scrapy-fake-useragent)
- [scrapy-proxies](https://github.com/aivarsk/scrapy-proxies)

**To run scrapy and store it in reports directory:**
```
scrapy crawl <spider_name> -o /reports/<report_name>.csv
```
