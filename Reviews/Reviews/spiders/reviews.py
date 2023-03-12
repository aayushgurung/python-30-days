import scrapy
import re
import json
class reviews_spider(scrapy.Spider):
    name='image_link'
    handle_httpstatus_list = [404, 500]
    def start_requests(self):
        with open('C:/Users/Nirajan/Desktop/python 30 days/datacollectionrestaurants/json files/location_test.json') as f:
             data =json.load(f)
        original_urls=[item['link'] for item in data]
        for url in original_urls:
            yield scrapy.Request(url=url,callback=self.parse)
    def parse(self,response):
        image_url = response.css('img.basicImg::attr(data-lazyurl)').extract()[:4]
        name=response.css('h1[data-test-target="top-info-header"]::text').extract_first('')
        cuisine=response.css('div.SrqKb::text').extract()
        Type=response.css('a.dlMOJ::text').extract()
        location = response.css('span.yEWoV::text').get()
        average_rating=response.xpath('//span[@class="ZDEqb"]/text()').get()
        number_of_reviews=response.xpath('//a[@class="IcelI"]/text()').get()
        if average_rating is not None and number_of_reviews is not None:
            average_rating=float(average_rating)
            number_of_reviews=int(number_of_reviews)
        else:
            average_rating=0
            number_of_reviews=0
        
        #Reviews Details
        final_rating={}
        review_url=response.url
        meta={
                                'url':review_url,
                                'name':name ,
                                'image_url':image_url,
                                'cuisine':cuisine,
                                'Type': Type,     
                                'location':location,
                                'final_rating':final_rating,
                                'average_rating':average_rating,
                                'number_of_reviews':number_of_reviews,
        }
        
        yield scrapy.Request(url=review_url,callback=self.parse_reviews,
                             meta=meta)
    def parse_reviews(self,response):
        final_rating=response.meta['final_rating']
        username=[]
        rating=[]
        partial_entry=[]
        list_container=response.xpath(".//div[contains(@class,'listContainer')]")
        for review in  list_container.xpath(".//div[contains(@class,'review-container')]"):
            temp_username=review.xpath(".//div[@class='info_text pointer_cursor']/div/text()").get()
            temp_rating= float(review.xpath(".//span[contains(@class, 'bubble_')]/@class").re_first(r'bubble_(\d+)'))/10.0,
            temp_partial_entry= review.xpath(".//p[@class='partial_entry']/text()").get()
            username.append(temp_username)
            rating.append(temp_rating)
            partial_entry.append(temp_partial_entry)
        for i in range(len(username)):
            final_rating[username[i]] = {'rated': rating[i], 'comment': partial_entry[i]}
        next=response.xpath("//a[contains(@class,'next')]/@href").get()
        if next is not None:
            next_review_link='https://www.tripadvisor.com/'+next
        else:
            next_review_link=response.url
        if next_review_link is not None and next is not None:
            meta={
                 'url':response.meta['url'],
                'name':response.meta['name'] ,
                'image_url':response.meta['image_url'] ,
                'cuisine':response.meta['cuisine'] ,
                'Type': response.meta['Type'] ,     
                'location':response.meta['location'] ,
                'final_rating':final_rating,
                'average_rating':response.meta['average_rating'],
                'number_of_reviews': response.meta['number_of_reviews'] ,
            }
            yield scrapy.Request(url=next_review_link,callback=self.parse_reviews,meta=meta)
        else:
            yield {
                    'url':response.meta['url'],
                    'name':response.meta['name'] ,
                    'location':response.meta['location'] ,
                    'image_url':response.meta['image_url'] ,
                    'cuisine':response.meta['cuisine'] ,
                    'Type': response.meta['Type'] ,  
                    'average_rating':response.meta['average_rating'],
                    'number_of_reviews': response.meta['number_of_reviews'] , 
                    'rating':final_rating ,   

                    }
