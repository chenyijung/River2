#Sqlite logic testing
#using

import sqlite3
import pandas as pd
import InspectRule as IR
conn = sqlite3.connect('db.sqlite3')
#cursor = conn.execute("riverName")
df=pd.read_sql_query("select * from RiverInspect_riverinspectmodel ", conn)
df_export=pd.read_sql_query("select * from RiverInspect_riverinspectexport",conn)

#print("\n BEFORE \n" ,df)

length_table=len(df) #探測table長度

i=0    #定義迴圈起始
while i<length_table:   #定義迴圈終點
#    print(df.loc[i,"stationName"],"\n")  #迴圈中逐項顯示資料
    df_export.loc[i,"id"]=int(i+1)      #將id標註於新table
#    print("\n DF_RAW == ",df.loc[i,"inspectO2"],"==")
#    print("\n IR_point == ",IR.RPI(df.loc[i,"inspectO2"],df.loc[i,"inspectBOD"],df.loc[i,"inspectSS"],df.loc[i,"inspectN2"]) ,"==\n")
    df_export.loc[i,"stationName"]=df.loc[i,"stationName"]
    df_export.loc[i,"inspectO2"]=IR.RPI_O2(df.loc[i,"inspectO2"])
    df_export.loc[i,"inspectBOD"]=IR.RPI_BOD(df.loc[i,"inspectBOD"])
    df_export.loc[i,"inspectSS"]=IR.RPI_SS(df.loc[i,"inspectSS"])
    df_export.loc[i,"inspectN2"]=IR.RPI_N2(df.loc[i,"inspectN2"])
    df_export.loc[i,"RPI_Point"]=IR.RPI(df.loc[i,"inspectO2"],df.loc[i,"inspectBOD"],df.loc[i,"inspectSS"],df.loc[i,"inspectN2"])  #將資料轉入新table
    df_export.loc[i,"RPI_Result"]=IR.RPIInspect(df_export.loc[i,"RPI_Point"])  #將資料轉入新table

    i=i+1                                                 #迴圈下一項

df_export.to_sql('RiverInspect_riverinspectexport',con=conn,if_exists='replace',index=False)
#print ("\n ==================== \n" , df_export) #將寫好的dataframe寫回sqlite的 database
conn.close() #關閉連結
print("\t Processed ")

#print("\n RPI == ",IR.RPIInspect(5),"==\n")
