import os
from typing import Any, Dict, Generator, List

import pytest
import yaml
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy_utils import database_exists, drop_database
from app.drivers.rdb.init_db import init_db
from sqlalchemy.orm import sessionmaker, scoped_session

from app.drivers.rdb.base import Base
from app.main import app


def load_fixtures(db: scoped_session, path: str) -> None:
    with open(path, "r") as f:
        data: List[Dict[str, Any]] = yaml.load(f, Loader=yaml.FullLoader)
        init_db(db, data)


@pytest.fixture(scope="function")
def SessionLocal() -> Generator:
    # settings of test database
    TEST_SQLALCHEMY_DATABASE_URL = "sqlite:///./test_temp.db"
    engine = create_engine(
        TEST_SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
    )

    assert not database_exists(
        TEST_SQLALCHEMY_DATABASE_URL
    ), "Test database already exists. Aborting tests."

    # Create test database and tables
    Base.metadata.create_all(engine)
    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

    # Run the tests
    yield SessionLocal

    # Drop the test database
    drop_database(TEST_SQLALCHEMY_DATABASE_URL)


@pytest.fixture(scope="module")
def client() -> Generator:
    with TestClient(app) as c:
        yield c
