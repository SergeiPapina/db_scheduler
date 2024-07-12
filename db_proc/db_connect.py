from sqlalchemy import create_engine
from sqlalchemy_utils import database_exists, create_database
from db_orm import create_tables, Author, Article

user = 'postgres'
password = ''
host = 'localhost'
port = 5432
database = 'oim_db_temp'


def get_connection():
    engine = create_engine(
        url="postgresql://{0}:{1}@{2}:{3}/{4}".format(
            user, password, host, port, database
        )
    )
    print(f"successfully connected to {database} ")
    if not database_exists(engine.url):
        create_database(engine.url)
        print(f"craeted new database {database}")
        create_tables(engine)
        print(f"created tables {Author.__tablename__}, {Article.__tablename__}")

    return engine

