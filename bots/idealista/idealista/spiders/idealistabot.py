# -*- coding: utf-8 -*-
import scrapy
import re

class IdealistabotSpider(scrapy.Spider):
    name = 'idealista'
    allowed_domains = ['idealista.com']
    #start_urls=['https://www.idealista.com/alquiler-viviendas/madrid-madrid/']

    def __init__(self, *args, **kwargs):
        urls = kwargs.pop('urls', [])
        if urls:
            self.start_urls = urls.split(',')
        #self.logger.info(self.start_urls)
        super(IdealistabotSpider, self).__init__(*args, **kwargs)
        
    def parse(self, response):

        print("RESPONSE")
        print(response)

        url_selector = '//div[@class="item-info-container"]/a/@href'
        url_content = response.xpath(url_selector).extract()

        for i in url_content:
            url = "https://idealista.com"+str(i)
            yield scrapy.Request(url = url, callback = self.parse_item)
        
        next_pag_selector = '//a[@class="icon-arrow-right-after"]/@href'
        next_pag = response.xpath(next_pag_selector).extract()

        yield scrapy.Request(url = next_pag[0])

    def parse_item(self, response):
        selector_name = '//span[@class="main-info__title-main"]/text()'
        name_content = response.xpath(selector_name).extract()

        selector_price = '//span[@class="info-data-price"]/text()'
        price_content = response.xpath(selector_price).extract()

        selector_space = '//div[@class="info-features"]/span/span/text()'
        space_content = response.xpath(selector_space).extract()

        selector_address = '//span[@class="main-info__title-minor"]/text()'
        address_content = response.xpath(selector_address).extract()

        selector_images = '//div[@id="multimedia-container"]'
        images_content = response.xpath(selector_images).extract()

        selector_features = '//div[@class="details-property_features"]/ul/li/text()'
        features_content = response.xpath(selector_features).extract()
        
        selector_company = '//div[@class="professional-name"]/span/text()'
        company_content = response.xpath(selector_company).extract()

        text = response.text

        # property images are loaded via javascript, so we need to parse the js code using regex
        image_list = re.findall(r'imageDataService:"+(.*?)(?:,WEB_DETAIL|$)', text, re.DOTALL)
        feature_list = features_content
        address = address_content[0]
        price = price_content[0]
        name = name_content[0]
        space = space_content[0]
        rooms = space_content[1]
        company = company_content[0]
        url = response.url
