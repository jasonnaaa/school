import datetime

week_6_date = datetime.date(2021, 10, 4)
print(week_6_date)

#this is just a string not a a date
week_6_date = "2021-10-04"

# doesnt like leading 0's
week_6_date = datetime.date(2021, 10, 04)
print(week_6_date)

import datetime
date_today = datetime.date.today()
print(date_today)
print(date_today.day)
print(date_today.month)
print(date_today.year)

date_out_week = datetime.timedelta(days=7)
print(date_today + date_out_week)
print(date_today - date_out_week)

import datetime
mydate = datetime.datetime(2021, 10, 31, 12, 00, 30, 100)
print(mydate)
print(mydate.year)
print(mydate.month)
print(mydate.day)
print(mydate.hour)
print(mydate.minute)
print(mydate.microsecond)

import datetime
date_today = datetime.date.today()
date_1=date_today.today()
date_2=datetime.datetime.now()
date_3=datetime.datetime.utcnow()
print(date_today)
print(date_1)
print(date_2)
print(date_3)

import datetime
date_utc = datetime.datetime.utcnow()
print(date_utc)
date_central = date_utc.astimezone()
print(date_central)

# formatting

import datetime
date_1 = datetime.date.today()
d1 = date_1.strftime("%d/%m/%Y")
print("d1 = ", d1)

d2 = date_1.strftime("%B, %d %Y")
print("d2 = ", d2)

d3 = date_1.strftime("%m/%d/%y")
print("d3 = ", d3)

d4 = date_1.strftime("%b-%d-%Y")
print("d4 = ", d4)

import datetime
date_string = "10-31-2021 12:30:20"
date_date = datetime.datetime.strptime(date_string, "%m-%d-%Y %H:%H:%S")

#formats must match, doesnt work
date_string = "October-31-2021"
date_date = datetime.datetime.strptime(date_string, "%m-%d-%Y")

import datetime
date_string = "10-31-2021 12:30:10"
date_string2 = "4-15-2019 11:20:10"
date_date = datetime.datetime.strptime(date_string, "%m-%d-%Y %H:%H:%S")
date_date2 = datetime.datetime.strptime(date_string2, "%m-%d-%Y %H:%H:%S")
print(date_date - date_date2)