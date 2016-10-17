import scrapy

class lnSpider(scrapy.Spider):
    name = 'lnSpider'
    allowded_domains = ['loopnet.com']
    start_urls = []
    f = open("urls.txt","r")
    urlList = f.read().splitlines()
    for url in urlList:
        start_urls.append(url)

    def parse(self, response):
        i = 0
        for item in response.xpath('//table[@class="property-data"]'):
            if i == 0:
                yield {'item': item.xpath('.//td/text()').extract()}
            i += 1
        pass
