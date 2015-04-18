# -*- coding: utf-8 -*-

# Scrapy settings for scrawlBilibill project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'scrawlBilibill'

SPIDER_MODULES = ['scrawlBilibill.spiders']
NEWSPIDER_MODULE = 'scrawlBilibill.spiders'
CONCURRENT_REQUESTS = 1
CONCURRENT_REQUESTS_PER_DOMAIN = 1
# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'scrawlBilibill (+http://www.yourdomain.com)'
