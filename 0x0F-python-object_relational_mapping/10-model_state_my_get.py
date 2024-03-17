#!/usr/bin/python3
"""model state sqlalchemy"""

from sqlalchemy import create_engine
from model_state import Base, State
from sys import argv
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    username = argv[1]
    password = argv[2]
    database_name = argv[3]
    state_name = argv[4]
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.
                           format(username, password, database_name),
                           pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()

    query = session.query(State).filter(State.name.ilike(state_name))\
        .order_by(State.id)
    records = query.all()

    if records:
        for record in records:
            print("{:d}".format(record.id))
    else:
        print("Not found")
