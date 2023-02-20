import scrapy

class reviews_spider(scrapy.Spider):

    name='review'
  
    def start_requests(self):
        urls=['https://www.tripadvisor.com/Restaurant_Review-g293890-d2343431-Reviews-Kathmandu_Grill_Restaurant_And_Wine_Bar-Kathmandu_Kathmandu_Valley_Bagmati_Zone_C.html',
         'https://www.tripadvisor.com/Restaurant_Review-g293890-d17433340-Reviews-Lavie_Garden-Kathmandu_Kathmandu_Valley_Bagmati_Zone_Central_Region.html',
         'https://www.tripadvisor.com/Restaurant_Review-g293890-d13157284-Reviews-Carpe_Diem_Lounge_Bakery-Kathmandu_Kathmandu_Valley_Bagmati_Zone_Central_Region.html',
         'https://www.tripadvisor.com/Restaurant_Review-g293890-d16923231-Reviews-MarcoPolo_Restaurant-Kathmandu_Kathmandu_Valley_Bagmati_Zone_Central_Region.html',
         'https://www.tripadvisor.com/Restaurant_Review-g293890-d18916031-Reviews-French_Creperie_Kathmandu-Kathmandu_Kathmandu_Valley_Bagmati_Zone_Central_Region.html',
         'https://www.tripadvisor.com/Restaurant_Review-g293890-d13625935-Reviews-Yala_Cafe-Kathmandu_Kathmandu_Valley_Bagmati_Zone_Central_Region.html',
         'https://www.tripadvisor.com/Restaurant_Review-g293890-d839336-Reviews-Green_Organic_Cafe_and_Farmers_Bar-Kathmandu_Kathmandu_Valley_Bagmati_Zone_Central.html',
         'https://www.tripadvisor.com/Restaurant_Review-g293890-d16711979-Reviews-Upstairs_Cafe-Kathmandu_Kathmandu_Valley_Bagmati_Zone_Central_Region.html',
         'https://www.tripadvisor.com/Restaurant_Review-g293890-d12067637-Reviews-Thamel_Doner_Kebab-Kathmandu_Kathmandu_Valley_Bagmati_Zone_Centraeviews-Places_Restaurant_Bar-Kathmandu_Kathmandu_Valley_Bagmati_Zone_Central_Region.html',
         'https://www.tripadvisor.com/Restaurant_Review-g293890-d4090661-Reviews-Rosemary_Kitchen_And_Coffee_Shop-Kathmandu_Kathmandu_Valley_Bagmati_Zone_Central_.html',
         'https://www.tripadvisor.com/Restaurant_Review-g293890-d1155247-Reviews-Toran_Restaurant-Kathmandu_Kathmandu_Valley_Bagmati_Zone_Central_Region.html',
         'https://www.tripadvisor.com/Restaurant_Review-g293890-d1155303-Reviews-La_Dolce_Vita-Kathmandu_Kathmandu_Valley_Bagmati_Zone_Central_Region.html',
         'https://www.tripadvisor.com/Restaurant_Review-g293890-d7181862-Reviews-Sarangi_Vegetarian_Restaurant-Kathmandu_Kathmandu_Valley_Bagmati_Zone_Central_Reg.html',
         'https://www.tripadvisor.com/Restaurant_Review-g293890-d6123527-Reviews-The_Best_Kathmandu_Kitchen-Kathmandu_Kathmandu_Valley_Bagmati_Zone_Central_Region.html',
         'https://www.tripadvisor.com/Restaurant_Review-g293890-d12714029-Reviews-Paleti_Bhanchha_Ghar_Restaurant_Bar-Kathmandu_Kathmandu_Valley_Bagmati_Zone_Cent.html',
         'https://www.tripadvisor.com/Restaurant_Review-g293890-d3445538-Reviews-Mitho_Restaurant-Kathmandu_Kathmandu_Valley_Bagmati_Zone_Central_Region.html',
         'https://www.tripadvisor.com/Restaurant_Review-g293890-d1099376-Reviews-Cafe_Mitra_Restaurant_Bar-Kathmandu_Kathmandu_Valley_Bagmati_Zone_Central_Region.html',
         'https://www.tripadvisor.com/Restaurant_Review-g293890-d4327738-Reviews-Western_Tandoori_Naan_House-Kathmandu_Kathmandu_Valley_Bagmati_Zone_Central_Regio.html',
         'https://www.tripadvisor.com/Restaurant_Review-g293890-d23822217-Reviews-Avocado_Cafe_Thamel-Kathmandu_Kathmandu_Valley_Bagmati_Zone_Central_Region.html']
        for url in urls:
            yield scrapy.Request(url=url,callback=self.parse)

    def parse():
        pass

    pass