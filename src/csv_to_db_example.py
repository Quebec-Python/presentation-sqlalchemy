# coding: utf-8

import os
import csv
from glob import glob
from datetime import datetime

from db import User, connect, init_db

CSV_PATH = os.path.join("..", "data", "*.csv")
CSV_FILES = glob(CSV_PATH)
CSV_FILES.reverse()


if __name__ == '__main__':
    init_db()
    session = connect(debug=True)

    for csv_file in CSV_FILES:
        with open(csv_file) as f:
            csv_content = csv.DictReader(f)

            session.add_all((
                User(
                    nas=row["nas"],
                    country=row["country"],
                    fullname=row["fullname"],
                    # Tue Dec 31 1996 11:35:43
                    created_at=datetime.strptime(
                        row["created_at"], "%a %b %d %Y %H:%M:%S"
                    ).date(),
                    birthday=datetime.strptime(
                        row["birthday"], "%d/%m/%Y"
                    ).date(),
                    email=row["email"]
                ) for row in csv_content
            ))

    session.commit()