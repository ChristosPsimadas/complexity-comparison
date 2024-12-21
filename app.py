import os
import sqlite3

from flask import Flask, request, jsonify, send_from_directory

app = Flask(__name__)

DB_PATH = 'complexity_classes.db'


def query_relationship(class_a, class_b):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    query = """
    WITH RECURSIVE containment AS (
        SELECT class_a, class_b FROM relationships WHERE class_a = ?
        UNION ALL
        SELECT r.class_a, r.class_b
        FROM relationships r
        INNER JOIN containment c ON r.class_a = c.class_b
    )
    SELECT * FROM containment WHERE class_b = ?;
    """

    cursor.execute(query, (class_a,class_b))
    rows = cursor.fetchall()
    conn.close()

    return len(rows) > 0



@app.route('/api/relationship', methods=['GET'])
def get_relationship():
    #if you get an error check these names
    class_a = request.args.get('classA')
    class_b = request.args.get('classB')

    if class_a is None or class_b is None:
        return jsonify({"relationship":"unknown"}), 400

    if query_relationship(class_a, class_b):
        return jsonify({"relationship":"a subset"}), 200
    else:
        return jsonify({"relationship":"unknown"}), 200

@app.route('/')
def serve_index():
    return send_from_directory(os.getcwd(), 'index.html')

@app.route('/script.js')
def serve_index2():
    return send_from_directory(os.getcwd(), 'script.js')

@app.route('/style.css')
def serve_css():
    return send_from_directory(os.getcwd(), 'style.css')

if __name__ == '__main__':
    app.run(debug=True)