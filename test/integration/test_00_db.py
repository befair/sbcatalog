import pymongo

from settings import *


def test_prepare_db():
    try:
        conn = pymongo.connection.Connection(MONGO_HOST, MONGO_PORT)
        if 'sbcatalog-bak' in conn.database_names():
            conn.drop_database('sbcatalog-bak')
        if MONGO_DBNAME in conn.database_names():
            conn.copy_database(MONGO_DBNAME, 'sbcatalog-bak')
            conn.drop_database(MONGO_DBNAME)
        assert True
    except:
        assert False
