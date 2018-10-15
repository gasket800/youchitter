# coding: utf-8

import config
import datetime
import json
from requests_oauthlib import OAuth1Session
import psycopg2


CK = config.CONSUMER_KEY
CS = config.CONSUMER_SECRET
AT = config.ACCESS_TOKEN
ATS = config.ACCESS_TOKEN_SECRET

ENDPOINT = config.ENDPOINT
PORT = config.PORT
DBNAME = config.DBNAME
USER = config.USER
PASSWD = config.PASSWD

twitter = OAuth1Session(CK, CS, AT, ATS)
url = 'https://api.twitter.com/1.1/search/tweets.json'
word = 'うんこ'.decode('utf-8')
params = {'count': 100, 'q': word}

res = twitter.get(url, params=params)

if res.status_code == 200:
    tweets = json.loads(res.text)

    try:
        access = 'dbname=%s host=%s port=%s user=%s password=%s' % (DBNAME, ENDPOINT, PORT, USER, PASSWD)
        conn = psycopg2.connect(access)
        cur = conn.cursor()

        for tweet in tweets['statuses']:
            # created_at = tweet['created_at']
            created_at = datetime.datetime.strptime(tweet['created_at'], '%a %b %d %H:%M:%S +0000 %Y')
            text = tweet['text']
            sql = 'insert into boo_data (text, created_at) values (%s, %s)'

            try:
                cur.execute(sql, (text, created_at))

            except psycopg2.DataError as e:
                pass

            finally:
                conn.commit()

    except psycopg2.DatabaseError as e:
        print(e)

    finally:
        conn.close()

else:
    print("Failed: %d" % res.status_code)
