import sqlite3

conn =sqlite3.connect(':memory:')
c = conn.cursor()
c.execute(""" CREATE TABLE T1(
              Portfolio text,
              Holding text,
              Weight NUMERIC
              )""")

data_T1 = [('peter parker', 'spider', 59),
           ('steve rogers', 'shield', 85),
           ('tony stark', 'iron', 75),
           ('Thor', 'hammer', 92),
           ('peter parker', 'spider', 59),
           ('steve rogers', 'shield', 85),
           ('peter parker', 'spider', 59),
           ('steve rogers', 'shield', 85),
           ('peter parker', 'spider', 59),
           ('steve rogers', 'shield', 85),
           ('peter parker', 'spider', 59),
           ('steve rogers', 'shield', 85),
           ('peter parker', 'spider', 59),
           ('steve rogers', 'shield', 85),
           ('peter parker', 'spider', 59),
           ('steve rogers', 'shield', 85),
           ('peter parker', 'spider', 59),
           ('steve rogers', 'shield', 85),
           ('peter parker', 'spider', 59),
           ('steve rogers', 'shield', 85),
           ('peter parker', 'spider', 59),
           ('steve rogers', 'shield', 85),
           ('peter parker', 'spider', 59),
           ('steve rogers', 'shield', 85),
           ('peter parker', 'spider', 59),
           ('steve rogers', 'shield', 85),
           ]

c.executemany("INSERT INTO T1 VALUES(?,?,?)",data_T1)

conn.commit()

conn.commit()
c.execute("SELECT Portfolio, SUM(Weight) FROM T1 GROUP BY Portfolio HAVING COUNT(Portfolio)>=10")
c = c.fetchall()
print(c)