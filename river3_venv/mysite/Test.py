#Sqlite logic testing
#using

import sqlite3
import pandas as pd
conn = sqlite3.connect('db.sqlite3')
#cursor = conn.execute("riverName")
df=pd.read_sql_query("select * from RiverStationBasic_riverstation ", conn)
print("\n BEFORE \n" ,df)

i=0

while i!=1:
    print(df.loc[i,"TestData1"],"\n")
    i=i+1

#print ("Name = " , row[0])
