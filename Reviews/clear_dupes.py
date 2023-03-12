import json
from scrapy.utils.request import request_fingerprint
from scrapy.http import Request
from scrapy.utils.project import get_project_settings
from scrapy.utils.job import job_dir
from scrapy.dupefilters import RFPDupeFilter
from scrapy import Spider
from scrapy.crawler import CrawlerProcess

# Replace 'urls.json' with the path to your JSON file.
class MySpider(Spider):
    name = "myspider"    
    with open('C:/Users/Nirajan/Desktop/python 30 days/datacollectionrestaurants/json files/location_test.json') as f:
        data = json.load(f)
    start_urls=[item['link'] for item in data]

spider_instance=MySpider()
process=CrawlerProcess()
settings = process.settings
dupefilter = RFPDupeFilter.from_settings(settings)
# dupefilter.job_dir = job_dir(settings)
dupefilter.log("Clearing dupefilter's fingerprint cache",spider=spider_instance)

# for url in original_urls:
#     request = Request(url)
#     fp = request_fingerprint(request, include_headers=True)
#     dupefilter.fingerprints.clear()
#     dupefilter.file_fingerprints.clear()
#     dupefilter.fingerprints_to_delete = set()
#     dupefilter.request_seen(request)
#     dupefilter.persist(request)

# dupefilter.log("Done clearing dupefilter's fingerprint cache",spider=Spider)
