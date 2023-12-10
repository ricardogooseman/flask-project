from flask import Flask,jsonify
from settings import (DB_NAME,USER_NAME,PASSWORD)
from api.models import Listing,HouseRules
import psycopg2

app = Flask(__name__)


@app.route('/listings')
def listings():
    conn = psycopg2.connect(database = DB_NAME, user = USER_NAME, password = PASSWORD)
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM listings LIMIT 1;')
    listings_records = cursor.fetchall()
    return jsonify([Listing(listing).__dict__ for listing in listings_records])

@app.route('/listings/<listing_id>')
def listings_byId(listing_id):
    conn = psycopg2.connect(database = DB_NAME, user=USER_NAME,password=PASSWORD)
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM listings WHERE listing_id= %s;',(listing_id,))
    listings = cursor.fetchall()
    return jsonify([Listing(listing).__dict__ for listing in listings])

@app.route('/listings/houserules/<allowed_or_not>')
def find_matching_listings(allowed_or_not):
    conn = psycopg2.connect(database = DB_NAME, user = USER_NAME,password = PASSWORD)
    cursor = conn.cursor()
    #pattern = f'%{allowed_or_not}%'
    cursor.execute("SELECT host_name, listing_id, house_rules FROM listings WHERE house_rules LIKE %s;",(f'%{allowed_or_not}%',))
    listings = cursor.fetchall()
    return jsonify([HouseRules(listing).__dict__ for listing in listings])

app.run(debug = True)
