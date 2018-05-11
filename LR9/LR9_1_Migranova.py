import sqlite3
import sys

db_file_path = sys.argv[1]
n = int(sys.argv[2])

conn = sqlite3.connect(db_file_path)
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


run_query(queries[n])

conn.close()

