from db_orm import Article, Author
from datetime import datetime

ezz = Author(
    firstname="Ezzeddin",
    lastname="Abdullah",
    email="ezz_email@gmail.com"
)

ahmed = Author(
    firstname="Ahmed",
    lastname="Mohammed",
    email="ahmed_email@gmail.com"
)

serg = Author(
    firstname="Sergei",
    lastname="Papina",
    email="papina.sergei@gmail.com"
)

article1 = Article(
    slug="article_1",
    title="about article1",
    content="Content of article1",
    author=ezz
)

article2 = Article(
    slug="article_2",
    title="about article2",
    content="One more content of article2",
    created_on=datetime(2022, 8, 29),
    author=ezz
)

article3 = Article(
    slug="article_3",
    title="about article3",
    content="content for article3",
    author=ahmed
)

article4 = Article(
    slug="article_4",
    title="about article4",
    content="inner content of article4",
    author=ahmed
)

article5 = Article(
    slug="article_5",
    title="about article5",
    content="inner content of article5",
    author=serg
)


def session_commit(session, article):
    session.add(article)
    session.commit()


def session_flush(session, article_list):
    for _ in article_list:
        session.add(_)

    session.flush()


def session_add_all(session, article_list):
    session.add_all(article_list)
    # session.flush()


def update_value(session):
    query = session.query(Article)
    filtered_query = query.filter(Article.slug == "article_2")
    filtered_query.update({Article.title: "Hahaha!"})
    # filtered_query.first()
    session.commit()
