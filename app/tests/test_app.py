import os
from typing import Any, Dict, Generator, List

import pytest
import yaml
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session

from app.drivers.api.endpoints.user import get_db
from app.drivers.models.base import Base
from app.drivers.models.init_db import init_db
from app.main import app

client = TestClient(app)


def load_fixtures(db: scoped_session, path: str) -> None:
    with open(path, "r") as f:
        data: List[Dict[str, Any]] = yaml.load(f, Loader=yaml.FullLoader)
        init_db(db, data)


@pytest.fixture(scope="function")
def db() -> Generator:

    # settings of test database
    TEST_SQLALCHEMY_DATABASE_URL: str = "sqlite:///./test.db"
    engine = create_engine(
        TEST_SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
    )

    # Create test database and tables
    Base.metadata.create_all(engine)
    db = scoped_session(sessionmaker(autocommit=False, autoflush=False, bind=engine))

    file_path: str = os.path.join(os.path.dirname(__file__), "db", "db.yaml")
    load_fixtures(db, file_path)

    def override_get_db() -> Generator:
        try:
            db_ = db()
            yield db_
        finally:
            db_.close()

    app.dependency_overrides[get_db] = override_get_db
    yield db
    app.dependency_overrides[get_db] = get_db
    Base.metadata.drop_all(bind=engine)


@pytest.fixture(scope="module")
def clients() -> Generator:
    with TestClient(app) as c:
        yield c
