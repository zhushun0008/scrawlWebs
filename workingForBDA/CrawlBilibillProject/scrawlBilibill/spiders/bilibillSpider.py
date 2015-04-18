__author__ = 'zhushun0008'
import scrapy
from scrawlBilibill.items import ScrawlbilibillItem
import json
import codecs
import os

class bilibillRankingSpider(scrapy.Spider):
    name = "bilibillRankingSpider"
    allowed_domains = ["bilibili.com"]
    ## Test implementation with just one url.
    # start_urls = ["http://www.bilibili.com/index/rank/all-1-0.json"]

    def genUrls(self):
        # sample url : http://www.bilibili.com/index/rank/all-1-0.json"

        urlPrefix = "http://www.bilibili.com/index/rank/"
        urlSuffix = ".json"
        # all
        # original
        # bangumi
        rankMenuType = ("all", "origin", "bangumi")

        rankCatalogyTid = ("0", "1", "3", "129", "4", "36", "5", "23", "119", "11")
        rankDateRange = ("1", "3", "7", "30")
        urlList = []
        for typeIndex in range(len(rankMenuType)):
            for rangeIndex in range(len(rankDateRange)):
                for tidIndex in range(len(rankCatalogyTid)):
                    tempType = rankMenuType[typeIndex]
                    tempRange = rankDateRange[rangeIndex]
                    tempTid = rankCatalogyTid[tidIndex]
                    if(tempType == "bangumi"):
                        tempType = "all"
                        tempTid = "33"

                    tempurl = urlPrefix +tempType + "-" + tempRange + "-" + tempTid + urlSuffix
                    print tempurl
                    urlList.append(tempurl)
        return urlList

    start_urls = genUrls(name)

    def parse(self, response):
        jsonData = json.loads(response.body)
        jsonDataInfo = jsonData['rank']['list']
        numVideos = len(jsonDataInfo)
        filename = response.url.split("/")[-2]
        with codecs.open(filename, "w", "utf-8") as f:
            for videoIndex in range(numVideos):
                item = ScrawlbilibillItem()
                # if videoIndex == 0:
                #     f.write('[')
                # else:
                #     f.write(',\n')
                # f.write('{')
                # f.write('"title": ')
                # f.write('"')
                # f.write(jsonDataInfo[videoIndex]['title'])
                # f.write('"')
                # f.write(', "play": ')
                # f.write(str(jsonDataInfo[videoIndex]['play']))
                # f.write(', "video_review": ')
                # f.write(str(jsonDataInfo[videoIndex]['video_review']))
                # f.write(', "author": ')
                # f.write(jsonDataInfo[videoIndex]['author'])
                # f.write(', "pts:" ')
                # f.write(str(jsonDataInfo[videoIndex]['pts']))
                # f.write('}')
                # f.write(',\n')
                item['title'] = jsonDataInfo[videoIndex]['title']
                item['play'] = jsonDataInfo[videoIndex]['play']
                item['video_review'] = jsonDataInfo[videoIndex]['video_review']
                item['author'] = jsonDataInfo[videoIndex]['author']
                item['pts'] = jsonDataInfo[videoIndex]['pts']
    #            print jsonDataInfo[videoIndex]['title']
                #f.write(jsonDataInfo[videoIndex]['title'])
                #f.write('\n')
                yield item
            #f.write(']')
            #f.close()



class bilibillVideoCounts1Spider(scrapy.Spider):
    name = "bilibillVideoCounts1Spider"
    allowed_domains = ["bilibili.com"]
    start_urls = ["http://www.bilibili.com"]

    def parse(self, response):
        secondCataUrlIist = response.xpath('//ul[@class="i_num"]/li').css(
            'a').xpath('@href').extract()
        filename = 'secondCataUrls2'
        with open(filename, 'w') as f:
            for urlIndex in range(len(secondCataUrlIist)):
                f.write('"' + self.start_urls[0] + str(secondCataUrlIist[
                    urlIndex]) + '",')
        f.write('\n')
        f.close()


class bilibillVideoCounts2Spider(scrapy.Spider):
    name = "bilibillVideoCounts2Spider"
    allowed_domains = ["bilibili.com"]
    urlPrefix = "http://www.bilibili.com"

    start_urls = ["http://www.bilibili.com/video/douga-mad-1.html",
                  "http://www.bilibili.com/video/douga-mmd-1.html","http://www.bilibili.com/video/douga-voice-1.html","http://www.bilibili.com/video/douga-else-1.html","http://www.bilibili.com/video/bangumi-two-1.html","http://www.bilibili.com/video/part-twoelement-1.html","http://www.bilibili.com/list/b--a--t----d---1.html","http://www.bilibili.com/video/music-Cover-1.html","http://www.bilibili.com/video/music-vocaloid-1.html","http://www.bilibili.com/video/music-perform-1.html","http://www.bilibili.com/video/music-coordinate-1.html","http://www.bilibili.com/video/music-video-1.html","http://www.bilibili.com/video/music-collection-1.html","http://www.bilibili.com/video/dance-1.html","http://www.bilibili.com/video/game-video-1.html","http://www.bilibili.com/video/game-ctary-1.html","http://www.bilibili.com/video/game-fight-1.html","http://www.bilibili.com/video/game-mugen-1.html","http://www.bilibili.com/video/tech-popular-science-1.html","http://www.bilibili.com/video/tech-future-1.html","http://www.bilibili.com/video/tech-wild-1.html","http://www.bilibili.com/video/tech-fun-1.html","http://www.bilibili.com/video/ent-life-1.html","http://www.bilibili.com/video/ent-animal-1.html","http://www.bilibili.com/video/ent-food-1.html","http://www.bilibili.com/video/ent-variety-1.html","http://www.bilibili.com/video/ent-korea-1.html","http://www.bilibili.com/video/douga-kichiku-1.html","http://www.bilibili.com/video/ent-Kichiku-1.html","http://www.bilibili.com/video/kichiku-manual_vocaloid-1.html","http://www.bilibili.com/video/kichiku-course-1.html","http://www.bilibili.com/video/movie-movie-1.html","http://www.bilibili.com/video/tv-micromovie-1.html","http://www.bilibili.com/video/movie-presentation-1.html","http://www.bilibili.com/video/soap-three-1.html","http://www.bilibili.com/video/tv-drama-1.html","http://www.bilibili.com/video/tv-sfx-1.html","http://www.bilibili.com/video/tv-presentation-1.html"]

    def parse(self, response):
        thirdLevelUrlList = response.xpath('//ul[@class="channellist"]').css(
            'a').xpath('@href').extract()

        parentUrl = response.url
        filename = 'thirdCataUrls02.txt'
        f = open(filename, 'a+')
        if len(thirdLevelUrlList) != 0:
            for urlIndex in range(len(thirdLevelUrlList)):
                f.write('"' + self.urlPrefix + str(thirdLevelUrlList[urlIndex]) + '",')
        else:
            f.write('"' + str(parentUrl) + '"' + ', ')

        f.close()


class bilibillVideoCounts3Spider(scrapy.Spider):
    name = "bilibillVideoCounts3Spider"

    allowed_domains = ["bilibili.com"]
    start_urls = ["http://www.bilibili.com/video/douga-mad-1.html",
                  "http://www.bilibili.com/video/douga-mmd-1.html", "http://www.bilibili.com/video/douga-voice-1.html","http://www.bilibili.com/video/douga-voice-original-1.html","http://www.bilibili.com/video/douga-voice-translate-1.html","http://www.bilibili.com/video/douga-else-1.html","http://www.bilibili.com/video/douga-else-handwriting-1.html","http://www.bilibili.com/video/douga-else-information-1.html","http://www.bilibili.com/video/douga-else-tattle-1.html","http://www.bilibili.com/video/douga-else-other-1.html","http://www.bilibili.com/video/bangumi-two-1.html","http://www.bilibili.com/video/newbangumi-ova-1.html","http://www.bilibili.com/video/part-twoelement-1.html","http://www.bilibili.com/video/bangumi-ova-1.html","http://www.bilibili.com/list/b--a--t----d---1.html", "http://www.bilibili.com/video/music-Cover-1.html", "http://www.bilibili.com/video/music-vocaloid-1.html","http://www.bilibili.com/video/music-vocaloid-vocaloid-1.html","http://www.bilibili.com/video/music-vocaloid-utau-1.html","http://www.bilibili.com/video/music-vocaloid-chinese-1.html","http://www.bilibili.com/video/music-perform-1.html", "http://www.bilibili.com/video/music-coordinate-1.html", "http://www.bilibili.com/video/music-video-1.html","http://www.bilibili.com/video/music-oped-1.html","http://www.bilibili.com/video/music-video-other-1.html","http://www.bilibili.com/video/music-collection-1.html", "http://www.bilibili.com/video/dance-1.html", "http://www.bilibili.com/video/game-video-1.html","http://www.bilibili.com/video/game-presentation-1.html","http://www.bilibili.com/video/game-video-other-1.html","http://www.bilibili.com/video/gmv-1.html","http://www.bilibili.com/video/game-ctary-1.html","http://www.bilibili.com/video/game-ctary-standalone-1.html","http://www.bilibili.com/video/game-ctary-network-1.html","http://www.bilibili.com/video/game-ctary-handheld-1.html","http://www.bilibili.com/video/game-ctary-other-1.html","http://www.bilibili.com/video/game-fight-1.html","http://www.bilibili.com/video/game-fight-matches-1.html","http://www.bilibili.com/video/game-fight-explain-1.html","http://www.bilibili.com/video/game-fight-other-1.html","http://www.bilibili.com/video/game-mugen-1.html", "http://www.bilibili.com/video/tech-popular-science-1.html","http://www.bilibili.com/video/tech-geo-bbc-1.html","http://www.bilibili.com/video/tech-geo-discovery-1.html","http://www.bilibili.com/video/tech-geo-national-1.html","http://www.bilibili.com/video/tech-geo-nhk-1.html","http://www.bilibili.com/video/tech-geo-other-1.html","http://www.bilibili.com/video/tech-future-1.html","http://www.bilibili.com/video/tech-future-digital-1.html","http://www.bilibili.com/video/tech-future-military-1.html","http://www.bilibili.com/video/tech-future-mobile-1.html","http://www.bilibili.com/video/tech-future-other-1.html","http://www.bilibili.com/video/tech-wild-1.html","http://www.bilibili.com/video/tech-otaku-1.html","http://www.bilibili.com/video/tech-geo-course-1.html","http://www.bilibili.com/video/figure-1.html","http://www.bilibili.com/video/tech-fun-1.html","http://www.bilibili.com/video/speech-1.html","http://www.bilibili.com/video/course-1.html","http://www.bilibili.com/video/tech-humanity-1.html","http://www.bilibili.com/video/tech-funvideo-1.html","http://www.bilibili.com/video/ent-life-1.html", "http://www.bilibili.com/video/ent-animal-1.html","http://www.bilibili.com/video/ent-animal-cat-1.html","http://www.bilibili.com/video/ent-animal-dog-1.html","http://www.bilibili.com/video/ent-animal-other-1.html","http://www.bilibili.com/video/ent-food-1.html","http://www.bilibili.com/video/ent-food-video-1.html","http://www.bilibili.com/video/ent-food-course-1.html","http://www.bilibili.com/video/ent-variety-1.html", "http://www.bilibili.com/video/ent-korea-1.html","http://www.bilibili.com/video/ent-korea-music-dance-1.html","http://www.bilibili.com/video/ent-korea-variety-1.html","http://www.bilibili.com/video/ent-korea-other-1.html","http://www.bilibili.com/video/douga-kichiku-1.html", "http://www.bilibili.com/video/ent-Kichiku-1.html", "http://www.bilibili.com/video/kichiku-manual_vocaloid-1.html", "http://www.bilibili.com/video/kichiku-course-1.html", "http://www.bilibili.com/video/movie-movie-1.html", "http://www.bilibili.com/video/tv-micromovie-1.html", "http://www.bilibili.com/video/movie-presentation-1.html", "http://www.bilibili.com/video/soap-three-1.html","http://www.bilibili.com/video/soap-three-cn-1.html","http://www.bilibili.com/video/soap-three-jp-1.html","http://www.bilibili.com/video/soap-three-us-1.html","http://www.bilibili.com/video/soap-three-oth-1.html","http://www.bilibili.com/video/tv-drama-1.html","http://www.bilibili.com/video/tv-drama-cn-1.html","http://www.bilibili.com/video/tv-drama-jp-1.html","http://www.bilibili.com/video/tv-drama-us-1.html","http://www.bilibili.com/video/tv-drama-other-1.html","http://www.bilibili.com/video/tv-sfx-1.html","http://www.bilibili.com/video/tv-sfx-sfx-1.html","http://www.bilibili.com/video/tv-sfx-pili-1.html","http://www.bilibili.com/video/tv-presentation-1.html"]
    def parse(self, response):
        totalVideos = response.xpath('//div[@class="pagelistbox"]/span/text('
                                     ')').re('[0-9]+')[1]
        domainUrl ='http://www.bilibili.com'

        parentUrl = response.url
        nameTag ='//a[@href="' + str(response.url[len(domainUrl):]) + '"]' + \
            '/text()'
        cata = str(response.xpath(nameTag).extract())
        filename = 'numVideos02.txt'
        f = open(filename, 'a+')
        f.write(cata)
        f.write(':\t' + str(totalVideos) + '\n')
        f.close()

class bilibiliSpaceSpider(scrapy.Spider):

    name = "bilibiliSpaceSpider"

    allowed_domains = ["bilibili.com"]
    start_urls = []
    lastIndex = [3, 8, 8, 22, 23, 5, 87, 631, 15, 3, 2, 4, 5]
    urlPrefix = ["http://space.bilibili.com/space?uid=779665&page=",
                 "http://space.bilibili.com/space?uid=833133&page=",
                 "http://space.bilibili.com/space?uid=374377&page=",
                 "http://space.bilibili.com/space?uid=777964&page=",
                 "http://space.bilibili.com/space?uid=585267&page=",
                 "http://space.bilibili.com/space?uid=425642&page=",
                 "http://space.bilibili.com/space?uid=79&page=",
                 "http://space.bilibili.com/space?uid=1324413&page=",
                 "http://space.bilibili.com/space?uid=673816&page=",
                 "http://space.bilibili.com/space?uid=213741&page=",
                 "http://space.bilibili.com/space?uid=684169&page=",
                 "http://space.bilibili.com/space?uid=313485&page=",
                 "http://space.bilibili.com/space?uid=109&page="]

    urlPrefix2 = ["http://space.bilibili.com/space?uid=433351&page=",
                  "http://space.bilibili.com/space?uid=256157&page=",
                  "http://space.bilibili.com/space?uid=2095062&page=",
                  "http://space.bilibili.com/space?uid=139905&page=",
                  "http://space.bilibili.com/space?uid=1492811&page=",
                  "http://space.bilibili.com/space?uid=168598&page=",
                  "http://space.bilibili.com/space?uid=216025&page=",
                  "http://space.bilibili.com/space?uid=19653&page=",
                  "http://space.bilibili.com/space?uid=690883&page=",
                  "http://space.bilibili.com/space?uid=546195&page=",
                  "http://space.bilibili.com/space?uid=675926&page=",
                  "http://space.bilibili.com/space?uid=748709&page=",
                  "http://space.bilibili.com/space?uid=116683&page=",
                  "http://space.bilibili.com/space?uid=381738&page=",
                  "http://space.bilibili.com/space?uid=1605721&page=",
                  "http://space.bilibili.com/space?uid=3295&page=",
                  "http://space.bilibili.com/space?uid=3400459&page=",
                  "http://space.bilibili.com/space?uid=131145&page=",
                  "http://space.bilibili.com/space?uid=201434&page=",
                  "http://space.bilibili.com/space?uid=2643893&page=",
                  "http://space.bilibili.com/space?uid=88358&page=",
                  "http://space.bilibili.com/space?uid=236260&page=",
                  "http://space.bilibili.com/space?uid=4396774&page=",
                  "http://space.bilibili.com/space?uid=188758&page=",
                  "http://space.bilibili.com/space?uid=227787&page=",
                  "http://space.bilibili.com/space?uid=256763&page=",
                  "http://space.bilibili.com/space?uid=675926&page=",
                  "http://space.bilibili.com/space?uid=739077&page=",
                  "http://space.bilibili.com/space?uid=1322259&page=",
                  "http://space.bilibili.com/space?uid=646007&page=",
                  "http://space.bilibili.com/space?uid=3476650&page=",
                  "http://space.bilibili.com/space?uid=2976992&page=",
                  "http://space.bilibili.com/space?uid=132704&page=",
                  "http://space.bilibili.com/space?uid=488736&page=",
                  "http://space.bilibili.com/space?uid=808171&page=",
                  "http://space.bilibili.com/space?uid=1492&page=",
                  "http://space.bilibili.com/space?uid=387549&page=",
                  "http://space.bilibili.com/space?uid=4162287&page="]

    lastIndex2 = [8, 23, 2, 5, 4, 20, 12, 1339, 7, 4, 5, 9, 5, 1950, 3, 8, 3,
                  2, 5, 3, 6, 9, 12, 9, 8, 50, 5, 16, 6, 15, 7, 4, 1, 5, 6,
                  21, 13, 5]
    lastIndex3 = [8, 23, 2]
    urlPrefix3 = ["http://space.bilibili.com/space?uid=433351&page=",
                  "http://space.bilibili.com/space?uid=256157&page=",
                  "http://space.bilibili.com/space?uid=2095062&page="]



    for i in range(len(lastIndex2)):
        for j in range(lastIndex2[i]):
            start_urls.append(urlPrefix2[i] + str(j+1))


    def parse(self, response):
        thisUrl = response.url
        uidStartQuote = thisUrl.find('uid=')+4
        uidEndQuote = thisUrl.find('&', uidStartQuote)
        uidForThisUrl = int(thisUrl[uidStartQuote:uidEndQuote])

        videoUrlForOnePage = response.xpath('//a[@class="title"]').xpath('@href').extract()
        videoNamesForOnepage = response.xpath('//a[@class="title"]/text('
                                              ')').extract()
        VideoDateForOnePafe = response.xpath('//div[@class="c"]/text()').extract()


        fupInfor = codecs.open('upInfor.txt', "r+", "utf-8")
        allInes = fupInfor.readlines()
        upInforList = []

        for line in allInes:
            upInforList.append(line.split('\t'))
        fupInfor.close()

        for i in range(len(upInforList)):
            if int(upInforList[i][3]) == uidForThisUrl:
                UpNumber = upInforList[i][0]
                UpName = upInforList[i][1]
                UpUrl = upInforList[i][2]
                break


        filename = 'nameDateUr4.txt'
        f = codecs.open(filename, "a+", "utf-8")

        for i in range(len(videoNamesForOnepage)):

            f.write(UpNumber)
            f.write('\t')
            f.write(UpName)
            f.write('\t')
            f.write(UpUrl)
            f.write('\t')
            f.write(videoNamesForOnepage[i])
            f.write('\t')
            f.write(VideoDateForOnePafe[i][5:])
            f.write('\t')
            f.write(videoUrlForOnePage[i])
            f.write('\n')
        f.close()




# upIdsfileName = 'upids,txt'
# f = open(upIdsfileName, "a+")
# for i in range(len(urlPrefix2)):
#     tempurl= urlPrefix2[i]
#     startUidQuote = tempurl.find('uid=') + 4
#     endUidQupte = tempurl.find('&', startUidQuote)
#     tempUid = tempurl[startUidQuote:endUidQupte]
#     f.write(tempUid)
#     f.write('\n')
# f.close()
#
#


