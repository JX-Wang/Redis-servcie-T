# usr/bin/env python
# coding:utf-8

import redis

try:
    r = redis.Redis(host="39.106.165.57", port=6379, db=0)
    r.get("msg")
except Exception as e:
    print "Connect Error as -> ", str(e)

