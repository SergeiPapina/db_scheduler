from sqlalchemy import create_engine
from sqlalchemy_utils import database_exists, create_database
from sqlalchemy.engine import URL
import urllib

user = 'postgres'
password = 'kolonka'
host = 'localhost'
port = 5432
database = 'oim_db_temp'


def get_connection_mssql():
    connection_string = ("DRIVER={ODBC Driver 18 for SQL Server};Server=tcp:127.0.0.1,1433;Database=ComponentDB;Uid=papina;"
                         "Pwd=$@#Fa34YeP#3BBbS7#Q&!54c*9YXHR9$V5E9EKk&C!OL7hLKo&;Encrypt=yes;"
                         "TrustServerCertificate=yes;Connection Timeout=30;")
    connection_url = URL.create("mssql+pyodbc", query={"odbc_connect": connection_string})
    engine = create_engine(connection_url)

    print(f"successfully connected to {connection_string.split(';')[2]} ")
    if not database_exists(engine.url):
        create_database(engine.url)
        print(f"created new database {database}")
        create_tables(engine)
        print(f"created tables {Author.__tablename__}, {Article.__tablename__}")

    return engine

get_connection_mssql()