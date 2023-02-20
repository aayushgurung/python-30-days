import scrapy

class restaurantlinkspider(scrapy.Spider):
    name='res_link'

    frontlink='https://www.tripadvisor.com'

    def start_requests(self):
        urls=['https://www.tripadvisor.com/Restaurants-g293890-Kathmandu_Kathmandu_Valley_Bagmati_Zone_Central_Region.html',
                'https://www.tripadvisor.com/RestaurantSearch-g293890-oa30-Kathmandu_Kathmandu_Valley_Bagmati_Zone_Central_Region.html',
                'https://www.tripadvisor.com/RestaurantSearch-g293890-oa60-Kathmandu_Kathmandu_Valley_Bagmati_Zone_Central_Region.html',
                'https://www.tripadvisor.com/RestaurantSearch-g293890-oa90-Kathmandu_Kathmandu_Valley_Bagmati_Zone_Central_Region.html',
                'https://www.tripadvisor.com/RestaurantSearch-g293890-oa120-Kathmandu_Kathmandu_Valley_Bagmati_Zone_Central_Region.html',
                'https://www.tripadvisor.com/RestaurantSearch-g293890-oa150-Kathmandu_Kathmandu_Valley_Bagmati_Zone_Central_Region.html',
                'https://www.tripadvisor.com/Restaurants-g293891-or30-Pokhara_Gandaki_Zone_Western_Region.html',
                'https://www.tripadvisor.com/Restaurants-g293891-or60-Pokhara_Gandaki_Zone_Western_Region.html',
                'https://www.tripadvisor.com/Restaurants-g293891-or90-Pokhara_Gandaki_Zone_Western_Region.html',
                'https://www.tripadvisor.com/Restaurants-g293891-or120-Pokhara_Gandaki_Zone_Western_Region.html',
                'https://www.tripadvisor.com/Restaurants-g293891-or150-Pokhara_Gandaki_Zone_Western_Region.html',
                'https://www.tripadvisor.com/Restaurants-g293891-or180-Pokhara_Gandaki_Zone_Western_Region.html',
                'https://www.tripadvisor.com/Restaurants-g293891-or210-Pokhara_Gandaki_Zone_Western_Region.html',
                'https://www.tripadvisor.com/Restaurants-g293891-or240-Pokhara_Gandaki_Zone_Western_Region.html',
                'https://www.tripadvisor.com/Restaurants-g293891-or270-Pokhara_Gandaki_Zone_Western_Region.html',
                'https://www.tripadvisor.com/Restaurants-g293891-or300-Pokhara_Gandaki_Zone_Western_Region.html',
                'https://www.tripadvisor.com/Restaurants-g293891-or330-Pokhara_Gandaki_Zone_Western_Region.html',
                'https://www.tripadvisor.com/Restaurants-g293891-or360-Pokhara_Gandaki_Zone_Western_Region.html',
                'https://www.tripadvisor.com/Restaurants-g293891-or390-Pokhara_Gandaki_Zone_Western_Region.html',
                'https://www.tripadvisor.com/Restaurants-g293891-or420-Pokhara_Gandaki_Zone_Western_Region.html',

                ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self,response):
        for link in response.css('a.Lwqic.Cj.b'):
            yield {
                'link': link.css('a.Lwqic.Cj.b').attrib['href'],
            }


