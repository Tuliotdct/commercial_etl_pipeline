from sqlalchemy import create_engine
from sqlalchemy.engine import URL
from db_credentials import get_secret


def db_connection():

    secrets = get_secret()

    url_connection = URL.create(
        drivername='postgresql+psycopg2',
        username=secrets['username'],
        password=secrets['password'],
        host=secrets['host'],
        port=secrets['port'],
        database=secrets['dbname']
    )
    try:
        engine_connection = create_engine(url_connection)
        print("Database connection established successfully")
    except SQLAlchemyError as e:
        print(f'Failed to connect to the database. Error {e}')

    return engine_connection
