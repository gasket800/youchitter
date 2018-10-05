# -*- coding: utf-8 -*-

import config
import json
from requests_oauthlib import OAuth1Session

CK = config.CONSUMER_KEY
CS = config.CONSUMER_SECRET
AT = config.ACCESS_TOKEN
ATS = config.ACCESS_TOKEN_SECRET

twitter = OAuth1Session(CK, CS, AT, ATS)

url = 'https://api.twitter.com/1.1/search/tweets.json'

word = 'うんこ'.decode('utf-8')

params = {'count': 10, 'q': word}
res = twitter.get(url, params=params)

if res.status_code == 200:
    timelines = json.loads(res.text)
    print timelines['statuses'][0]['created_at']
    print timelines['statuses'][0]['text']
    print '-' * 100
else:
    print("Failed: %d" % res.status_code)


