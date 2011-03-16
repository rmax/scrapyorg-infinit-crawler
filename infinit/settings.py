# Scrapy settings for infinit project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/topics/settings.html
#

BOT_NAME = 'infinit'
BOT_VERSION = '1.0'

SPIDER_MODULES = ['infinit.spiders']
NEWSPIDER_MODULE = 'infinit.spiders'
DEFAULT_ITEM_CLASS = 'infinit.items.InfinitItem'
USER_AGENT = '%s/%s' % (BOT_NAME, BOT_VERSION)

