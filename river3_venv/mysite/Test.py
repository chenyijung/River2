#Sqlite logic testing
#using

import sqlite3
import pandas as pd
conn = sqlite3.connect('db.sqlite3')
#cursor = conn.execute("riverName")
df=pd.read_sql_query("select * from RiverStationBasic_RiverStation ", conn)
print("\n BEFORE \n" ,df)

table_length=len(df)
i=0

while i<table_length:
    print(df.loc[i,"id"],"\n")
    i=i+1

df_export.loc[]=df
df_export.to_sql('OceanInspect_oceaninstpectexport',conn,if_exists='append')

print("***df***\n",df_export)
#print ("Name = " , row[0])
