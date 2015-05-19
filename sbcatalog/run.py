#!/usr/bin/env python

from flaskapp import XMLEve
from sys import argv


app = XMLEve()
app.debug = True

if __name__ == '__main__':
    if 'update-geodb' in argv:
        from geomatic import update_geo_db
        update_geo_db(verbose=True)
    else:
        app.run()
