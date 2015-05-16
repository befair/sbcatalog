import pymongo

def test_prepare_db():
    try:
        conn = pymongo.connection.Connection('localhost', 27017)
        if 'sbcatalog-bak' in conn.database_names():
            conn.drop_database('sbcatalog-bak')
        if 'sbcatalog' in conn.database_names():
            conn.copy_database('sbcatalog', 'sbcatalog-bak')
            conn.drop_database('sbcatalog')
        assert True
    except:
        assert False
