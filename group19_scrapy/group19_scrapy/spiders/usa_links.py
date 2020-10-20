import scrapy
# import datetime

# dt = datetime.datetime.date()
# date = dt.day() + dt.month() + dt.day

class CnnSpider(scrapy.Spider):
    name = "USA"
    
    def start_requests(self):
        start_urls = [
            'https://www.usatoday.com/'
        ]

    def parse(self, response):
        website = "usa_today"
        # filename = website + date
        with open(website, 'wb') as f:
            f.write(response.xpath('//a/@href').extract())