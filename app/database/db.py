import psycopg2

from ..config import db_config


conn = psycopg2.connect(
    dbname=db_config["dbname"],
    user=db_config["user"],
    password=db_config["password"],
    host=db_config["host"],
    port=5432,
)

# cursor = conn.cursor()
