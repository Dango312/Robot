import sqlite3
from datetime import datetime

connection = sqlite3.connect("logs.db")
cursor = connection.cursor()
curId = None

cursor.execute("CREATE TABLE IF NOT EXISTS logs(" \
                      "id INTEGER PRIMARY KEY," \
                      "start DATETIME NOT NULL," \
                      "end DATETIME," \
                      "start_number int NOT NULL" \
                      ");")


def insertLog(start_number: int):
    global curId
    print("INSERT", start_number)
    insert_log = f"INSERT INTO logs (start, start_number) VALUES ('{datetime.now()}', {start_number});"
    cursor.execute(insert_log)
    connection.commit()
    getId = "SELECT id FROM logs ORDER BY id DESC LIMIT 1;"
    res = cursor.execute(getId)
    curId = res.fetchone()[0]


def updateEndTime():
    update_end_time = f"UPDATE logs SET end = '{datetime.now()}' WHERE id = {curId};"
    cursor.execute(update_end_time)
    connection.commit()


def prepareData(rec: list) -> dict:
    return {'id': rec[0], 'start_datetime': rec[1], 'end_datetime': {rec[2]}, 'start_number': {rec[3]}}


