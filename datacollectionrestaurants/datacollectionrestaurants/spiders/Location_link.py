import scrapy
import json
import re

class restaurantlinkspider(scrapy.Spider):
    name='location_link'
    num=0
    handle_httpstatus_list = [301]
    # def start_requests(self):
    #     urls=[
    #    'https://www.tripadvisor.com/Restaurants-g293889-Nepal.html#LOCATION_LIST',

    #             ]
    #     for url in urls:
    #         yield scrapy.Request(url=url, callback=self.parse)

    # def parse(self,response):
    #     for link in response.xpath('//div[@class="geos_grid"]//a/@href').extract():
    #         lnk = 'https://www.tripadvisor.com' + link 
    #         yield {
    #             'link':lnk,
    #         }
    def start_requests(self):
        self.num=0
        with open('C:/Users/Nirajan/Desktop/python 30 days/datacollectionrestaurants/json files/location.json') as f:
            data=json.load(f)
        original_urls = [item['link'] for item in data]
        for url in original_urls:
            yield scrapy.Request(url=url, callback=self.parse)
            self.num=0

    def parse(self, response):
        modified_url=response.url
        for i in range(37):
            print(f"Parsing {modified_url}")
            yield scrapy.Request(modified_url,callback=self.parse_modified)
            modified_url= self.modify_url(response.url, i,self.num)
            self.num=self.num+30
        
    def parse_modified(self,response):
        if response.status == 301:
            self.logger.info(f"Ignoring 301 response for Url{self.num}")
            return
        for link in response.css('a.Lwqic.Cj.b'):
            yield {
                    'link': link.attrib['href'],
                }
        
    def modify_url(self,url,i,num):
        modified_url = re.sub(r'(?<=g)(\d+)(?=-)', r'\1-oa{}'.format(num), url)
        return modified_url

