from flask import Flask, render_template, jsonify
import random
import sqlite3


app = Flask(__name__)

def get_random_recommendation():
    conn = sqlite3.connect('recommendations.db')
    cursor = conn.cursor()
    cursor.execute('SELECT data, audience FROM recommendations ORDER BY RANDOM() LIMIT 1')
    row = cursor.fetchone()
    conn.close()
    if row:
        return {"recommendation": row[0], "audience": row[1]}
    return None
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/add')
def add():
    return render_template('add.html')

@app.route('/recommendation')
def recommendation():
    recommendation = get_random_recommendation()
    if recommendation:
        return jsonify({'recommendation': recommendation['recommendation'], 'audience': recommendation['audience']})
    return jsonify({'error': 'No recommendations found'}), 404

if __name__ == '__main__':
    from databaseINIT import init_db, populate_db
    init_db()
    populate_db()
    app.run(debug=True)