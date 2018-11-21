# -*- coding: utf-8 -*-
import json
class EXCELPipeline(object):
    def __init__(self):
        pass
        # self.filename = open("data.json", "a")

    def process_item(self, item, spider):
        # curTime = datetime.datetime.now()
        # text = json.dumps(dict(item), ensure_ascii=False) + ",\n"
        # self.filename.write(text.encode("utf-8"))
        f = open(item['id']+".json", "a+")
        text = json.dumps(dict(item), ensure_ascii=False) + ",\n"
        f.write(text.encode("utf-8"))
        f.close()
        return item

    def close_spider(self, spider):
        # import os
#         os.remove(self.filename)
#         self.work_book.save(self.filename)
        pass
        # self.work_book.Close(SaveChanges=0)