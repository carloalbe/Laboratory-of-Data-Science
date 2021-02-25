
import csv

ram_fact = open('data/ram_fact.csv', 'w', newline='')

cpu_fact = open('data/cpu_fact.csv', 'w', newline='')

gpu_fact = open('data/gpu_fact.csv', 'w', newline='')

files = [gpu_fact, cpu_fact, ram_fact]
objs = ['gpu_code','cpu_code','ram_code'] #sono le tre chiavi
cols = [['gpu_code','time_code','geo_code','vendor_code','sales_uds','sales_currency'],
        ['cpu_code','time_code','geo_code','vendor_code','sales_uds','sales_currency'],
        ['ram_code','time_code','geo_code','vendor_code','sales_uds','sales_currency']]
for i in range(3):
    files[i].truncate()
    csv.writer(files[i]).writerow(col for col in cols[i])
 


i = 0    #uso questo indici per iterare sulle tre liste prime definite 
with open("data/fact.csv",'r') as facts:
    reader = csv.DictReader(facts, delimiter=',')
    for row in reader: #sleggo riga tuto il csv 
        if row[objs[i]]=='': i+=1 #se trovo un valore nullo incremento i e mi sposto a destra ( da gpu a cpu e poi da cpu a ram)
        csv.writer(files[i]).writerow(row[col] for col in cols[i])
        
for j in range(3):
    files[j].close()
    
    
    
    
    