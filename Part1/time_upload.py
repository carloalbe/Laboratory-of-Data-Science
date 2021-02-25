
import csv 
import datetime

weekdays = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']
with open('data/time.csv','r+') as _csv:
 
    columns = ['time_code','year','month','day','week','quarter','day_of_week']
    reader = csv.DictReader(_csv)
    writer = csv.DictWriter(_csv, fieldnames=columns)
    writer.writeheader()
    for row in reader:
        quarter = str(int(row['month']) // 4)
        weekday = weekdays[int(datetime.datetime(int(row['year']),int(row['month']),int(row['day'])).weekday())]
        values = [row[value] for value in row]
        values.append(quarter)
        values.append(weekday)
        newrow = {col : value for col, value in zip(columns,values)}
        writer.writerow(newrow)