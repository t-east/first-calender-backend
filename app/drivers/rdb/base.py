from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, scoped_session
from pydantic import BaseSettings


class DBSettings(BaseSettings):
    host: str = "127.0.0.1"
    db_name = "calendar"
    user = "root"
    password = "password"

settings = DBSettings()

DATABASE: str = "mysql://%s:%s@%s/%s?charset=utf8" % (
    settings.user,
    settings.password,
    settings.host,
    settings.db_name,
)

ENGINE = create_engine(
    DATABASE,
    encoding = "utf-8",
    echo=True
)

Session = scoped_session(
    sessionmaker(
        autocommit = False,
        autoflush = False,
        bind = ENGINE
    )
)

Base = declarative_base()
Base.query = Session.query_property()

# modelで使用する
Base = declarative_base()

