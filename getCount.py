# coding: utf-8

import sys
import sqlite3
import datetime


conn = sqlite3.connect('boo_data.sqlite3')
sql = 'select created_at from boo_data order by created_at asc;'
data = conn.execute(sql)

counts = []
count = 0

# set_start_time = raw_input('input start time as yyyy-mm-dd hh:mm >> ')
set_start_time = sys.argv[1]

adjast_jst_time = datetime.timedelta(hours=9)

try:
    start_time = datetime.datetime.strptime(set_start_time, '%Y-%m-%d %H:%M')
    # start_time = start_time + adjast_jst_time

except Exception as e:
    print e
    sys.exit()

delta_time = datetime.timedelta(0, 60)
end_time = start_time + delta_time

print start_time

for i in data:
    tweet_time = datetime.datetime.strptime(i[0], '%Y-%m-%d %H:%M:%S') + adjast_jst_time

    if tweet_time < end_time:
        count += 1

    else:
        while tweet_time >= end_time:
            counts.append((end_time, count))
            end_time = end_time + delta_time
            count = 0
        count = 1

with open('./booTweetcount.data', 'w')as f:
    f.write('datetime,count \n')
    for k, v in counts:
        row_data = datetime.datetime.strftime(k, '%Y-%m-%d %H:%M:%S') + ',' + str(v) + '\n'
        f.write(row_data)


conn.close()
