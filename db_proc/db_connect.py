from sqlalchemy import create_engine
from sqlalchemy_utils import database_exists, create_database
from db_orm import create_tables, Author, Article
from sqlalchemy.engine import URL

user = 'postgres'
password = 'kolonka'
host = 'localhost'
port = 5432
database = 'oim_db_temp'


def get_connection_postgres():
    engine = create_engine(
        url="postgresql://{0}:{1}@{2}:{3}/{4}".format(
            user, password, host, port, database
        )
    )
    print(f"successfully connected to {database} ")
    if not database_exists(engine.url):
        create_database(engine.url)
        print(f"created new database {database}")
        create_tables(engine)
        print(f"created tables {Author.__tablename__}, {Article.__tablename__}")

    return engine


def get_connection_mssql():
    # connection_string = "DRIVER={SQL Server Native Client 10.0};SERVER=dagger;DATABASE=test;UID=user;PWD=password"
    connection_string = ("Driver={ODBC Driver 18 for SQL Server};Server=tcp:127.0.0.1,1433;Database=ComponentDB;Uid=root;"
                         "Pwd=9IkX1u#O%A$0z9P1f$Q3PGG0@LM2$WuDjY@SLSM54Z**G$w826;Encrypt=yes;"
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

