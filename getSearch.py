# -*- coding: utf-8 -*-

import config
import json
from requests_oauthlib import OAuth1Session
import sqlite3
from sqlite3 import Error


CK = config.CONSUMER_KEY
CS = config.CONSUMER_SECRET
AT = config.ACCESS_TOKEN
ATS = config.ACCESS_TOKEN_SECRET

twitter = OAuth1Session(CK, CS, AT, ATS)
url = 'https://api.twitter.com/1.1/search/tweets.json'
word = 'うんこ'.decode('utf-8')
params = {'count': 100, 'q': word}

res = twitter.get(url, params=params)

if res.status_code == 200:
    tweets = json.loads(res.text)

    try:
        conn = sqlite3.connect('boo_data.sqlite3')

        for tweet in tweets['statuses']:
            created_at = tweet['created_at']
            text = tweet['text']
            sql = 'insert into boo_data (text, created_at) values (?, ?)'
            conn.execute(sql, (text, created_at))

            print created_at
            print text
            print '-' * 100

        conn.commit()

    except Error as e:
        print(e)

    finally:
        conn.close()

else:
    print("Failed: %d" % res.status_code)
