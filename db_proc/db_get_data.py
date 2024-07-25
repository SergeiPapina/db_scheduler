def get_all(session, table):
    res = session.query(table).all()
    return res

# session.query(Article.slug, Article.title)[2]

# queries = session.query(Article)
# queries.first().id

# for article in session.query(Article).order_by(Article.title.desc()):
#     print(article.title)
