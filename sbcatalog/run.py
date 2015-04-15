#!/usr/bin/env python

from flaskapp import XMLEve


app = XMLEve()
app.debug = True

if __name__ == '__main__':
    app.run()

