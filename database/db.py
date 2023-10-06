import psycopg2


conn = psycopg2.connect(
    dbname=...,
    user=...,
    password=...,
    host=...,
    port=5432,
)

cursor = conn.cursor()
