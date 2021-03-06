# -*- coding: utf-8 -*-
import traceback

def get_allhit_url(page=1):
    return 'https://www.mturk.com/mturk/viewhits?selectedSearchType=hitgroups&sortType=LastUpdatedTime%3A1&&searchSpec=HITGroupSearch%23T%232%2310%23-1%23T%23!%23!LastUpdatedTime!1!%23!&pageNumber='+str(page)

def get_group_url(id):
   return "https://www.mturk.com/mturk/preview?groupId=%s" % id

def get_amazon_review_url(id):
    return "http://www.amazon.com/review/%s" % id

def grab_error(exc_info):
    return {
                'type': str(exc_info[0].__name__),
                'value': str(exc_info[1]),
                'traceback': unicode(traceback.extract_tb(exc_info[2]))
            }
