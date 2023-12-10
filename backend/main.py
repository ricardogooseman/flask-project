from flask import Flask,jsonify
from settings import DB_NAME
import psycopg2

app = Flask(__name__)


@app.route('/listings')
def listings():
    conn = psycopg2.connect(database = DB_NAME, user = 'ricardogooseman', password = 'postgres')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM listings;')
    listings_records = cursor.fetchall()
    return jsonify(listings_records)


app.run(debug = True)
