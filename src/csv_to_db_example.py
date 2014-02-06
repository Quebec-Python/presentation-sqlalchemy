# coding: utf-8

import os
import csv
from glob import glob
from datetime import datetime

from db import User, connect, init_db

CSV_PATH = os.path.join("..", "data", "*.csv")
csv_files = glob(CSV_PATH)
csv_files.reverse()

if __name__ == '__main__':
    init_db()
    session = connect(debug=True)

    # Pour chacun des fichiers csv dans le dossier data
    for csv_file in csv_files:
        # ouverture du fichier
        with open(csv_file) as f:
            # utilisation de DictReader pour transformer chaque ligne
            # du fichier texte en tableau avec des dictionnaires
            csv_content = csv.DictReader(f)

            # instanciation des users pour chaque ligne du DictReaders
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