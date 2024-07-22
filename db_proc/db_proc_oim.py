from db_connect import get_connection_postgres, get_connection_mssql
from sqlalchemy.orm import sessionmaker
from db_insert_data import *
from db_get_data import get_all
from db_orm import Article, Author
from db_oim_orm import Manufacturers, Capacitors


if __name__ == '__main__':
    print("hi")
    # engine = get_connection_postgres()
    engine = get_connection_mssql()

    Session = sessionmaker(bind=engine)
    session = Session()

    # session_commit(session, article5)
    # article_list = [article2, article3]
    # session_flush(session, article_list)
    # article_list.clear()
    # article_list.extend([article1, article4])
    # session_add_all(session, article_list)
    #
    # update_value(session)

    # manufacturers = get_all(session, Manufacturers)
    # for _ in manufacturers:
    #     print(_.ID, _.ManufacturerName)

    capacitors = get_all(session, Capacitors)
    for _ in capacitors:
        print(_.ID, _.ComponentName, _.OutputType, _.MinVoltage, _.MaxVoltage, _.MinCapacity, _.MaxCapacity,
              _.MinOperatingTemperature, _.MaxOperatingTemperature, _.AcceptableCapacityIncrease,
              _.AcceptableСapacityReduction, _.QualicationSG, _.QualicationЕС, _.Remark1, _.Remark2)


    # articles = get_all(session, Article)
    # for _ in articles:
    #     print(_.slug, _.title, _.content, _.author_id)
    #
    # authors = get_all(session, Author)
    # for _ in authors:
    #     print(_.id, _.firstname, _.lastname, _.email, len(_.author_articles))


