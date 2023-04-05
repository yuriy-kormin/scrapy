# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class VintedItem(scrapy.Item):
    id = scrapy.Field()
    price = scrapy.Field()
    service_fee = scrapy.Field()
    total_item_price = scrapy.Field()
    currency = scrapy.Field()