import pymongo

from settings import *


def test_restore_db():
    try:
        with pymongo.connection.Connection(MONGO_HOST, MONGO_PORT) as conn:
            conn.drop_database(MONGO_DBNAME)
            if 'sbcatalog-bak' in conn.database_names():
                conn.copy_database('sbcatalog-bak', MONGO_DBNAME)
                conn.drop_database('sbcatalog-bak')
            assert True
    except:
        assert False
