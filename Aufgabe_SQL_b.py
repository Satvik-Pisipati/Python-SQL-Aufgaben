import sqlite3
conn =sqlite3.connect(':memory:')
c = conn.cursor()
c.execute(""" CREATE TABLE T2(
             
              Holding text,
              Price NUMERIC,
              PriceDate NUMERIC
               
              )""")


data_T2 =[('xxx ',10000,197204),
                ('xxx ',150000,197205),
                ('xyk',10000,197206),
                ('xyz',10000,197207),
                ('xxx ',10000,197204),
                ('xxx ',150000,197205),
                ('xyk',10000,197206),
                ('xyz',10000,197207),
                ('xxx ',10000,197204),
                ('xxx ',150000,197205),
                ('xyk',10000,197206),
                ('xyz',10000,197207),
                ('xxx ',10000,197204),
                ('xxx ',150000,202005),
                ('xyk',10000,201906),
                ('xyz',10000,201907),
                ('xxx ',10000,200704),
                ('xxx ',150000,202005),
                ('xyk',10000,201806),
                ('xyz',10000,201907),
                ]
c.executemany("INSERT INTO T2 VALUES(?,?,?)",data_T2)

conn.commit()


conn.commit()
c.execute("SELECT Price,Holding ,MAX(PriceDate) FROM T2 GROUP BY Holding ")
c = c.fetchall()
print(c)