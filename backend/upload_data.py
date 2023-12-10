import psycopg2
from settings import (DB_NAME,USER_NAME,PASSWORD)
import pandas as pd

df = pd.read_csv('Airbnb_Open_Data.csv')
df.to_csv( path_or_buf="file1.csv")

conn = psycopg2.connect(database = DB_NAME, user = USER_NAME, password = PASSWORD)
cursor = conn.cursor()

with open("file1.csv","r") as f:
    cursor.copy_expert("COPY listings FROM STDIN WITH CSV HEADER",f)
    conn.commit()
