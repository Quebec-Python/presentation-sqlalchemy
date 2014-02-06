# SQLAlchemy

## a.k.a. La magie des ORMs

Repo Git: [http://goo.gl/so87LN](http://goo.gl/so87LN)

---

## ORM ?

### Object-Relational Mapper

---

## Object-Relational Mapper

* Technique de programmation
* correspondance entre monde objet (code) et monde relationnel (bd)

---

## Pourquoi ?

* Faire des requêtes SQL dans notre langage préféré
* Interface de programmation uniforme peu importe la source de données

<img src="static/img/orm.png" alt="">

---

## À quoi ressemble un model ?

    !python
    import sqlalchemy as sq
    from sq.ext.declarative import declarative_base
    from sq import Column, Integer, \
        String, DateTime, Date
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

---

## Comment établir une connexion à une base de données ?

    !python
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker

    engine = create_engine('sqlite:///:memory:')
    # mysql://user:pwd@localhost/dbname
    # oracle://user:pwd@localhost:port/dbname
    # mssql+pymssql://user:pwd@localhost:port/dbname
    SessionMakerInstance = sessionmaker(bind=engine)
    session = SessionMakerInstance()

---

## Comment obtenir des données ?

    !python
    # Select * from users;
    session.query(User).all()
    # Select * from users where fullname = "Bernard";
    session.query(User).filter(User.fullname="Bernard")

---

## Comment ajouter des données ?

    !python
    bernard = User(
        country="Canada",
        fullname="Bernard Chhun",
        created_at=datetime.now(),
    )
    session.add(bernard)
    session.commit()


---

## Comment modifier des données ?

    !python
    bernard.nas = 999999111
    session.commit()

---

## Comment supprimer des données ?

    !python
    session.delete(bernard)
    session.commit()

---

## Cas d'utilisation

### Lire une série de fichier CSV et insérer leur contenu dans la BD

    !bash
    $ cd src
    $ python csv_to_db_example.py