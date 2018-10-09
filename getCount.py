import sqlite3
import datetime


conn = sqlite3.connect('boo_data.sqlite3')
sql = 'select created_at from boo_data order by created_at asc;'
data = conn.execute(sql)

counts = []
count = 0

start_time = datetime.datetime.strptime('2018-10-05 12:20:00', '%Y-%m-%d %H:%M:%S')
end_time = start_time + datetime.timedelta(0, 60)

print start_time

for i in data:
    # print i
    h1 = datetime.datetime.strptime(i[0], '%a %b %d %H:%M:%S +0000 %Y')
    # h2 = h1 - start_time
    # print h2 if h2 >= datetime.timedelta() else 'x'
    # print h1 , h2 , datetime.timedelta(), datetime.timedelta(0, 60)

    if start_time <= h1 < end_time:
        count += 1

    if h1 >= end_time:
        # counts.append(end_time count)
        counts.append((end_time, count))
        end_time = end_time + datetime.timedelta(0, 60)
        count = 0

    print start_time, h1, end_time, count

for k, v in counts:
    print k, v

conn.close()
