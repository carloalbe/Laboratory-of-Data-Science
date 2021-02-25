
import pyodbc 
import csv

def isfloat(value):
  try:
    float(value)
    return True
  except ValueError:
    return False

server = 'tcp:apa.di.unipi.it' 
database = 'group17HWMart' 
username = 'group17' 
password = 't9lsb' 
connectionString = 'DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password

tables = [ 'Ram_product'] #'Time', is out cause need of tranformation 

cnxn = pyodbc.connect(connectionString)
for table in tables:
    with open('data/'+table+'.csv','r') as csv_table:
        rows = csv.DictReader(csv_table)
        
        cursor = cnxn.cursor()
        cursor.execute("SELECT * FROM "+ table )
        columns = '('
        types = []
        first = True
        if 'sales' in table or 'Time' in table : #devo leggere la prima colonna poiche nom è un 'identità'
            columns+=cursor.description[0][0]+','
        for column in cursor.description[1:]:
            columns += column[0] + ','
            types.append(column[1])
        
        print(types)
        columns = columns[:-1] + ')'
        cursor.close()
        print(columns)
        counter = 0
        for row in rows:
            
            cursor = cnxn.cursor()  #apro cursore
            values = '('
            for value in row:
                try:
                    if (row[value].isdigit() or isfloat(row[value])) and 'time' not in value:
                        if 'sales' in value: 
                            values += "'"+ str(row[value])[:str(row[value]).find('.')+3] + "', " 
                        elif 'code' in value: values += str(int(float(row[value]))) + ", "
                        else: values += str(row[value]) + ', '
                    else:
                        values += "'"+str(row[value]) + "', "
                except: print(value)
                    
            if 'sales' not in table and 'Time' not in table:
                values = '(' + values[values.find(' '):]
            values = values[:-2]+')'
            
        
       
            query = "INSERT INTO "+table+ " "+columns+" VALUES "+values
        #cursor.execute(query)
            try:
                cursor.execute(query)
                counter += 1
          
            except:
                print('ABORT',query)
                cursor.execute(query)
                cursor.close()
                cnxn.close()
            cursor.close() #chiudo cursore
            if counter == 500:
                print('COMMIT',query)
                cnxn.commit()
                counter = 0


    cnxn.commit()
        
cnxn.close()
