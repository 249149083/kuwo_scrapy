# -*- coding: utf-8 -*-
import time, datetime, calendar

def deep(d,key):
    ks = key.split('.')
    item = d
    for k in ks:
        if item.has_key(k):
            item = item[k]
        else:
            item = {}
            break

    return item

def delay_weekday(start_day = datetime.datetime.today(), weekday = calendar.MONDAY, forward = True):
    delay = datetime.timedelta(days = 1)
    ret_day = start_day

    while ret_day.weekday() != weekday:
        if forward:
            ret_day += delay
        else:
            ret_day -= delay

    return ret_day

