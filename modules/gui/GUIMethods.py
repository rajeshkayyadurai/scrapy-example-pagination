from bases.selectors import Selectors as sel
from modules.api.APIMethods import APIMethods

api = APIMethods()

# DSLR camera functions


def get_product_div_tags(response):
    return response.selector.xpath(sel.AmazonDict['Cameras']['DIV_CameraList'])


def get_discount_in_percent(div):
    return div.xpath(sel.AmazonDict['Cameras']['SPAN_DiscountInPercent']).re_first(r'\((.*)\)')


def get_details_page_url(div):
    return div.xpath(sel.AmazonDict['Cameras']['LNK_DetailPageURL']).extract_first()


def get_product_description(div):
    return div.xpath(sel.AmazonDict['Cameras']['TITLE_ProductDescription']).extract_first()


def get_product_old_price(div):
    return div.xpath(sel.AmazonDict['Cameras']['SPAN_ProductOldPrice']).extract_first()


def get_product_new_price(div):
    return div.xpath(sel.AmazonDict['Cameras']['SPAN_ProductNewPrice']).extract_first()