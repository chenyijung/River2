#Sqlite logic testing
#using

import sqlite3
import pandas as pd
conn = sqlite3.connect('db.sqlite3')
#cursor = conn.execute("riverName")
df=pd.read_sql_query("select * from RiverInspect_riverinspectmodel ", conn)
#print("\n BEFORE \n" ,df)

        
#print(df.index.stop)
#for i in range(int(df.index)):
#    print(i)

test_filter = df.loc [7,'inspectO2']

point = 0

if (test_filter<7):
    print("小於7")
    point=point+1
else:
    print("大於7")
    point=point+2
#df[ df['riverName']=='旱溪'] ]

print(test_filter)
print("點數為",point)



#i=0

#while i!=1:
#    print(df.loc[i,"TestData1"],"\n")
#    i=i+1

#print ("Name = " , row[0])

