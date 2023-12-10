import psycopg2
from settings import DB_NAME

conn = psycopg2.connect(database = DB_NAME, user = 'ricardogooseman', password = 'postgres')
cursor = conn.cursor()

with open("Airbnb_Open_Data.csv","r") as f:
    cursor.copy_expert("COPY listings FROM STDIN WITH CSV HEADER",f)
    conn.commit()
