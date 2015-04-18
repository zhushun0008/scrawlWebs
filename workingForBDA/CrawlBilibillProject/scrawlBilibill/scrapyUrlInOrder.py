__author__ = 'zhushun0008'
import scrapy

class mySpider(object):
    def __init__(self, myUrl):
        self.url = myUrl

    def crawlUrl(self, response):
        request = scrapy.Request(self.url,
                          callback=self.parsePage)

    def parsePage(self, response):
        totalVideos = response.xpath('//div[@class="pagelistbox"]/span/text('
                                     ')').re('[0-9]+')[1]
        domainUrl ='http://www.bilibili.com'

        parentUrl = response.url
        nameTag ='//a[@href="' + str(response.url[len(domainUrl):]) + '"]' + \
            '/text()'
        cata = str(response.xpath(nameTag).extract())
        filename = 'numVideos1.txt'
        f = open(filename, 'a+')
        f.write(cata)
        f.write(':\t' + str(totalVideos) + '\n')
        f.close()

aaa = mySpider("http://www.bilibili.com/video/douga-mad-1.html")
aaa.crawlUrl()

print "111"