# coding: utf-8

import os
import inspect
from datetime import datetime

from fabric.colors import red, green

from sqlite3 import dbapi2 as sqlite

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import (
    Column, Integer, String, DateTime, Date
)
from sqlalchemy import func

CURRENT_DIRECTORY = os.path.dirname(
    inspect.getfile(inspect.currentframe())
)

DATABASE_NAME = "users"

Base = declarative_base()

class User(Base):
    __tablename__ = "users"
    id = Column("id", Integer, primary_key = True)
    nas = Column("nas", Integer)
    country = Column("country", String(200))
    fullname = Column("fullname", String(200))
    created_at = Column("created_at", DateTime)
    birthday = Column("birthday", Date)
    email = Column("email", String(200))

def connect(debug=False):
    path = os.path.join(CURRENT_DIRECTORY, "{}.db".format(DATABASE_NAME))
    engine = create_engine(
        'sqlite+pysqlite:///{}'.format(path),
        module=sqlite,
        echo=debug
    )
    SessionMakerInstance = sessionmaker(bind=engine)
    return SessionMakerInstance()

def init_db():
    """
        Creates the database
    """
    path = os.path.join(CURRENT_DIRECTORY, "{}.db".format(DATABASE_NAME))

    # if the database file doesn't exist, let's create it
    if not os.path.isfile(path):
        sqlite.connect(path)
    else:
        print(red(u"La base de données existe déjà..."))
        print(red(u"Sa création est annulé"))
        return

    engine = create_engine('sqlite:///%s' % path, convert_unicode=True)
    Base.metadata.create_all(bind=engine)
    print(green(u"Base de données créé !"))

if __name__ == '__main__':
    print(green(u"Création de la base de données en cours..."))
    init_db()
    session = connect(debug=True)

    print(green(u"Combien d'usager dans la bd ?"))
    nb_user = len(session.query(User).all())

    print(green(
        u"Nombre d'usager dans la base de données: {}".format(nb_user)
    ))

    raw_input("On continue ?")

    print(
        green(u"Ajoutons 2 usagers...")
    )
    bernard = User(
        nas=123123123,
        country="Canada",
        fullname="Bernard Chhun",
        created_at=datetime.now(),
        birthday=datetime.strptime("1981/12/06", "%Y/%m/%d").date(),
        email="bernard.chhun@gmail.com"
    )
    john = User(
        nas=999111222,
        country="Canada",
        fullname="John Gosset",
        created_at=datetime.now(),
        birthday=datetime.strptime("1979/01/01", "%Y/%m/%d").date(),
        email="john.gosset@savoirfairelinux.com"
    )
    session.add(bernard)
    session.add(john)
    session.commit()

    print(
        green(u"Ajouté avec succès !")
    )

    raw_input("On continue ?")

    print(green(u"Combien d'usager dans la bd maintenant ?"))
    nb_user = len(session.query(User).all())
    print(green(
        u"Nombre d'usager dans la base de données: {}".format(nb_user)
    ))

    raw_input("On continue ?")

    print(
        green(u"Modifions la date de naissance de Bernard pour le 1 janvier 1966")
    )
    bernard.birthday = datetime.strptime("1966/01/01", "%Y/%m/%d").date()
    session.commit()

    print(
        green(
            u"Sa date de naissance est maintenant le {u.birthday}".format(
                u=bernard
            )
        )
    )

    raw_input("On continue ?")

    print(
        red(
            u"Supprimons maintenant Bernard de la base de données"
        )
    )

    session.delete(bernard)
    session.commit()

    print(green(u"Combien d'usager dans la bd maintenant ?"))
    nb_user = len(session.query(User).all())
    print(green(
        u"Nombre d'usager dans la base de données: {}".format(nb_user)
    ))

    session.close()
