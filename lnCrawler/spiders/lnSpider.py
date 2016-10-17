import scrapy

class lnSpider(scrapy.Spider):
    name = 'lnSpider'
    allowded_domains = ['loopnet.com']
    start_urls = []
    f = open("urls.txt","r")
    urlList = f.readlines()
    for url in urlList:
        start_urls.append(url)

    def parse(self, response):
        for table in response.xpath('//table[@class="property-data"]').extract_first():
            yield{'table':table}
        pass
