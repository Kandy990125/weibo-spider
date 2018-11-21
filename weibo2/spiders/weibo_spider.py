# -*- coding: utf-8 -*-
import scrapy
from weibo2.items import WeiboItem
import requests
import json
class WeibospiderSpider(scrapy.Spider):
    name = 'weibospider'
    allowed_domains = ['m.weibo.cn']
    start_urls = []
    # id_list = ["4301643686462756", "4301588208727148", "4301272716897769"]
    # 4307340167783933

    id_list = ["4307340167783933"]
    # 储存最新三条微博的id

    for id in id_list:
        # https://api.weibo.com/2/statuses/show.json
        # https://api.weibo.com/2/statuses/mentions.json
        # https://api.weibo.com/2/statuses/user_timeline.json
        # https://api.weibo.com/oauth2/access_token?client_id=YOUR_CLIENT_ID&client_secret=YOUR_CLIENT_SECRET&grant_type=authorization_code&redirect_uri=YOUR_REGISTERED_REDIRECT_URI&code=CODE
        # https://m.weibo.cn/api/statuses/repostTimeline?id=4301272716897769&page=1
        # comment_url = "https://m.weibo.cn/api/comments/show?id=%s" %(id)
        # start_urls.append("https://m.weibo.cn/api/statuses/show?id=%s" %(id))
        start_urls.append("https://m.weibo.cn/profile/info?uid=6068133006")
        # repost_url = "https://m.weibo.cn/api/statuses/repostTimeline?id=%s" %(id)
        # attitude_url = "https://m.weibo.cn/api/attitudes/show?id=%s" %(id)
        #         start_urls.append(comment_url)
        #         start_urls.append(repost_url)
        #         start_urls.append(attitude_url)

    def parse(self, response):
        text = response.body
        text = json.loads(text)
        i = 0
        # list_weibo_id = []
        while i < 3:
            # item = WeiboItem()
            id = text["data"]["statuses"][i]["id"]
            url = "https://m.weibo.cn/api/statuses/show?id=%s" %(id)
            # list_weibo_id.append(text["data"]["status"][str(i)]["retweeted_status"]["id"])
            # yield Request(url=url, meta={'item': item},callback=self.parse_item)
            res = requests.get(url)
            txt = json.loads(res.text)
            # print res.text
            item = WeiboItem()
            import datetime
            # now_time = datetime.datetime.now()
            item["time"] = str(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
            item["id"] = txt['idstr']
            item["repost"] = txt['reposts_count']
            item["att"]=txt['attitudes_count']
            item["comment"] = txt['comments_count']
            yield item
            i = i + 1
        # import datetime
        # now_time = datetime.datetime.now()
        # item["time"] = str(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
        # item["id"] = text['idstr']
        # item["repost"] = text['reposts_count']
        # item["att"]=text['attitudes_count']
        # item["comment"] = text['comments_count']
        # yield item
    # def parse_item(self,response):


