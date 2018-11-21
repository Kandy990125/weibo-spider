# from scrapy import cmdline
# cmdline.execute("scrapy crawl weibospider".split())

import time
import os

while True:
    os.system("scrapy crawl weibospider")
    time.sleep(1800)