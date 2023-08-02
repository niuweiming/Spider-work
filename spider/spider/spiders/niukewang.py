import scrapy
import time


class NiukeSpider(scrapy.Spider):
    name = 'niukewang'
    allow_domains = ["https://www.nowcoder.com/"]

    headers = {
    'User-Agent':
'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Mobile Safari/537.36 Edg/115.0.1901.183'
    }


    def start_requests(self):
        urls = [
                "https://www.nowcoder.com/jobs/school/jobs?",
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)


    def parse(self, response):
        filename = 'niukewang.html'
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log('Saved file %s' % filename)




class NiukeSpider(scrapy.Spider):
    name = 'BossSpider'
    allow_domains = ["https://www.zhipin.com"]

    headers = {
        'User-Agent':
'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Mobile Safari/537.36 Edg/115.0.1901.183'
    }


    def start_requests(self):
        urls = [
                "https://www.zhipin.com/taiyuan/",
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)


    def parse(self, response):
        filename = 'Boss.html'
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log('Saved file %s' % filename)