from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, scoped_session

# SQLALCHEMY_DATABASE_URL = "sqlite:///./sql_app.db"

host = "mysql:3306"
db_name = "calender"
user = "root"
password = "password"

# engine = create_engine(
#     SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
# )


DATABASE = "mysql://%s:%s@%s/%s?charset=utf8" % (
    user,
    password,
    host,
    db_name,
)

ENGINE = create_engine(DATABASE, encoding="utf-8", echo=True)

session = scoped_session(sessionmaker(autocommit=False, autoflush=False, bind=ENGINE))

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=ENGINE)
# SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
Base.query = session.query_property()

def get_db() -> Session:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()