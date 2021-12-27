import pymysql
import pandas as pd


conn = pymysql.connect(host='59.5.109.111', user='root', password='Isp0182292695@',
                       db='pnppos', charset='utf8')
 
curs = conn.cursor()

sql ="select * from TB_DBS_INFO"
curs.execute(sql)
rows = curs.fetchall()
print (rows)

result = pd.DataFrame(rows)
result
conn.close