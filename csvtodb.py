import pandas as pd
import mysql.connector 




x=pd.read_csv("attendance.csv")
columnNames=list(x)

for i in range(0,len(columnNames)-1):
    columnNames[i]=x[columnNames[i]].tolist()

for i in range(0,len(columnNames)-1):
    print(columnNames[i])

    
conn=mysql.connector.connect(host="localhost",username="root",password="1234",database="mini_projects")
my_cursor=conn.cursor()
for i in range(0,len(columnNames)-1):
    x=f"insert into StudentDatabase values ({},{},{});"
    my_cursor.execute(x)
    conn.commit()
conn.close()