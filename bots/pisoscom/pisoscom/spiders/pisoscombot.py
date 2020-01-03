# -*- coding: utf-8 -*-
import scrapy
import re
# scrapy crawl pisoscombot -a "urls=https://www.pisos.com/alquiler/pisos-madrid_sur/"

class PisoscombotSpider(scrapy.Spider):
    name = 'pisoscombot'
    allowed_domains = ['www.pisos.com']

    def __init__(self, *args, **kwargs):
        urls = kwargs.pop('urls', [])
        if urls:
            self.start_urls = urls.split(',')
        #self.logger.info(self.start_urls)
        super(PisoscombotSpider, self).__init__(*args, **kwargs)


    def parse(self, response):
        selector_item = '//div[@class="row  clearfix"]/@data-navigate-ref'
        item = response.xpath(selector_item).extract()
        base_url = "https://www.pisos.com/"

        selector_next_pag = '//a[@id="lnkPagSig"]/@href'
        next_pag_content = response.xpath(selector_next_pag).extract()
        
        for i in item:
            yield scrapy.Request(url = base_url+ str(i), callback = self.parse_item)

        u = base_url + str(next_pag_content[0])

        yield scrapy.Request(url = u , callback = self.parse)

    def parse_item(self, response):

        selector_price = '//div[@class="priceBox-price"]/span/text()'
        price_content = response.xpath(selector_price).extract()

        selector_name = '//div[@class="maindata-info"]/h1/text()'
        name_content = response.xpath(selector_name).extract()

        selector_address = '//h2[@class="position"]/text()'
        address_content = response.xpath(selector_address).extract()

        selector_basicinfo = '//div[@class="basicdata-info"]/div/text()'
        basicinfo_content = response.xpath(selector_basicinfo).extract()

        selector_property = '//div[@class="owner-data-info"]/a/text()'
        property_content = response.xpath(selector_property).extract()

        selector_gallery = '//input[@name="PhotosPath"]/@value'
        gallery_content = response.xpath(selector_gallery).extract()

        selector_basicatribs = '//li[@class="charblock-element element-with-bullet"]/span/text()'
        basicatribs_content = response.xpath(selector_basicatribs).extract()

        gallery_content = gallery_content[0].replace('!','').split(',')

        name = name_content[0]
        price =  re.findall(r'\d+', price_content[0])[0]
        space = re.findall(r'\d+', basicinfo_content[0])[0]
        address = address_content[0]
        rooms = re.findall(r'\d+', basicinfo_content[1])[0]   
        url = response.url

        '''
        #debug info:
        print(url)
        print(name)
        print(price)
        print(space)
        print(address)
        print(rooms)
        '''
        