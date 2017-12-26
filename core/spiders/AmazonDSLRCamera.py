import scrapy
from bases import URLs
from core.items import AmazonItem
from modules.gui import GUIMethods


class AmazonDSLRCamera(scrapy.Spider):
    name = "amazon-dslr-cameras"
    start_urls = URLs.AmazonDSLRCameras

    def parse(self, response):
        for div in GUIMethods.get_product_div_tags(response):
            item = AmazonItem()
            discount = GUIMethods.get_discount_in_percent(div)
            if discount is not None:
                absolute_url = GUIMethods.get_details_page_url(div)

                item['CATEGORY'] = 'Electronics'
                item['SUBCATEGORY'] = 'Camera'
                item['WEBSITE'] = 'Amazon'
                item['DESCRIPTION'] = GUIMethods.get_product_description(div),
                item['DISCOUNT'] = discount,
                item['OLD_PRICE'] = GUIMethods.get_product_old_price(div),
                item['NEW_PRICE'] = GUIMethods.get_product_new_price(div),
                item['PDP_URL'] = absolute_url

                yield item
