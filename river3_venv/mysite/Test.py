#Sqlite logic testing
#using

import sqlite3
import pandas as pd
import InspectRule as IR
conn = sqlite3.connect('db.sqlite3')
#cursor = conn.execute("riverName")
df=pd.read_sql_query("select * from OceanInspect_oceaninspectmodel ", conn)
df_export=pd.read_sql_query("select * from OceanInspect_oceaninspectexport",conn)
'''
print("\n BEFORE \n" ,df)

length_table=len(df) #探測table長度

i=0    #定義迴圈起始
while i<length_table:   #定義迴圈終點
#    print(df.loc[i,"stationName"],"\n")  #迴圈中逐項顯示資料
#    df_export.loc[i,"id"]=int(i+1)      #將id標註於新table
#    df_export.loc[i,"TestName"]=df.loc[i,"stationName"]  #將資料轉入新table
    i=i+1                                                 #迴圈下一項

df_export.to_sql('OceanInspect_oceaninspectexport',con=conn,if_exists='replace',index=False)
#print ("\n ==================== \n" , df_export) #將寫好的dataframe寫回sqlite的 database
conn.close() #關閉連結
'''
print("\n IR_point == ",IR.RPI(5,10,10,10),"==\n")
