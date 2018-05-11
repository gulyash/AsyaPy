import sqlite3


conn = sqlite3.connect('comp.db')
cursor = conn.cursor()

queries = [
    "select model, speed, hdd from pc where price<50000;",
    "select maker from product where type=\"printer\"",
    "select model, ram, screen from laptop where price>23000",
    "select * from printer where color=1",
    "select model, speed, hdd from laptop where screen=13 and price<22000"
]


def run_query(query):
    cursor.execute(query)
    results = cursor.fetchall()
    print(results)


for query in queries:
    run_query(query)

conn.close()

