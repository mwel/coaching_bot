from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import database_exists, create_database
from bot.constants import postgresql as settings

# check if db exists. If not, create one.
def get_engine(user, passwd, host, port, db):
    url = f"postgresql://{user}:{passwd}@{host}:{port}/{db}"
    if not database_exists(url):
        create_database(url)
    engine = create_engine(url, pool_size=50, echo=False)
    return engine

# create connector engine
engine = get_engine(settings['pguser'],
          settings['pgpasswd'],
          settings['pghost'],
          settings['pgport'],
          settings['pgdb'])

# Raise exception, if login data is bad. Else return login data.
def get_engine_from_settings():
    keys = ['pguser', 'pgpasswd', 'pghost', 'pgport', 'pgdb']
    if not all(key in keys for key in settings.keys):
        raise Exception('Bad config file')

    return get_engine(settings['pguser'],
          settings['pgpasswd'],
          settings['pghost'],
          settings['pgport'],
          settings['pgdb'])

#create session function
def get_session():
    engine = get_engine_from_settings()
    session = sessionmaker(bind=engine) ()
    return session

# actually create a session
session = get_session()

# close the session
session.close()

# clean up
engine = session.get_bind()
engine.dispose() # Close all checked in sessions