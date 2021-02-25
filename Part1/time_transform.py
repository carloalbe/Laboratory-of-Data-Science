
import csv 
import datetime

weekdays = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']
with open('data/time_.csv','r') as in_csv:
    with open('data/NewTime.csv','w') as out_csv:
        #le colonne che vorrei
        columns = ['time_code','year','month','day','week','quarter','day_of_week']
        reader = csv.DictReader(in_csv)
        writer = csv.DictWriter(out_csv, fieldnames=columns)
        writer.writeheader()
        for row in reader:
            values = [row[value] for value in row]   #salvo i valori esistenti 
            #cambio day e month in modo tale che siano rappresentati da due caratteri 
            #aggiungedo lo 0 davanti ai giorni e a mesi indicati tramite una sola cifra 
            if len(row['day'])==1:
                day = '0'+str(row['day'])
                values[3] = day
            if len(row['month'])==1:
                month = '0'+str(row['month'])
                values[2] = month
            #calcolo i valori per quarter e per weekday e li aggiungo alla lista dei valori
            quarter = str(int(row['month']) // 4 + 1)
            weekday = weekdays[int(datetime.datetime(int(row['year']),int(row['month']),int(row['day'])).weekday())]
            values.append(quarter)
            values.append(weekday)
            #scrivo la lista dei valori come nuova riga 
            newrow = {col : value for col, value in zip(columns,values)}
            writer.writerow(newrow)
            
            
            
            
            
            