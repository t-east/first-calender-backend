import os
from typing import Any, Dict, List

import yaml

from app.drivers.rdb.init_db import init_db
from app.drivers.rdb.base import SessionLocal


def main() -> None:
    db = SessionLocal()
    file_path = os.path.join(os.path.dirname(__file__), "db.yaml")
    with open(file_path, "r") as f:
        fixtures: List[Dict[str, Any]] = yaml.load(f, Loader=yaml.FullLoader)

    init_db(db, fixtures)


if __name__ == "__main__":
    main()
