#!/usr/bin/env python

from flaskapp import XMLEve
from sys import argv


app = XMLEve()

if __name__ == '__main__':
    if 'update-geodb' in argv:
        from geomatic import update_geo_db
        update_geo_db(verbose=True)
    else:
        app.run(host='0.0.0.0', port=8080)
