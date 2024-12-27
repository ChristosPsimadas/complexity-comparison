import json
import os
import sqlite3

from flask import Flask, request, jsonify

DB_PATH = 'complexity_classes.db'


def get_classes():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    query = """
    SELECT class_a FROM relationships
    UNION
    SELECT class_b FROM relationships; 
    """

    cursor.execute(query)
    rows = cursor.fetchall()
    conn.close()

    return rows



rows = get_classes()
parsedRows = []

for row in rows:
    parsedRows.append(row[0])

print(json.dumps(parsedRows))