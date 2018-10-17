# coding: utf-8

import config
import sys
# import sqlite3
import psycopg2
import datetime


ENDPOINT = config.ENDPOINT
PORT = config.PORT
DBNAME = config.DBNAME
USER = config.USER
PASSWD = config.PASSWD

access = 'dbname=%s host=%s port=%s user=%s password=%s' % (DBNAME, ENDPOINT, PORT, USER, PASSWD)
sql = 'select created_at from boo_data order by created_at asc;'

conn = psycopg2.connect(access)
cur = conn.cursor()
cur.execute(sql)

counts = []
count = 0

set_start_time = sys.argv[1]
adjast_jst_time = datetime.timedelta(hours=9)

try:
    start_time = datetime.datetime.strptime(set_start_time, '%Y-%m-%d %H:%M')

except Exception as e:
    print e
    sys.exit()

delta_time = datetime.timedelta(0, 60)
end_time = start_time + delta_time

for i in cur:
    tweet_time = i[0] + adjast_jst_time

    if tweet_time < end_time:
        count += 1

    else:
        while tweet_time >= end_time:
            counts.append((end_time, count))
            end_time = end_time + delta_time
            count = 0
        count = 1

with open('./booTweetcount_rs.data', 'w')as f:
    f.write('datetime,count \n')
    for k, v in counts:
        row_data = datetime.datetime.strftime(k, '%Y-%m-%d %H:%M:%S') + ',' + str(v) + '\n'
        f.write(row_data)


conn.close()

