import geocoder
import pymongo
import json


def get_addresses(verbose=False):
    with pymongo.connection.Connection() as conn:
        coll = conn['sbcatalog']['supplier']
        suppliers_in = coll.find()

    suppliers_out = []
    for s in suppliers_in:
        success = False
        x = {}
        x['name'] = s['name']
        a = s['address']
        # converting address to string
        address = ""
        for k in ['locality', 'zipcode', 'street']:
            if a[k]:
                address += a[k] + ' '
        address = address[:-1]
        if verbose:
            print('"' + address + '"', end=' ')
        # trying with full address
        result = geocoder.osm(address).json
        if result['status'] == 'OK' and result['country'] == 'Italia':
            success = True
        # trying with only city
        elif a['locality']:
            if verbose:
                print('NOT FOUND!  ' + '"' + a['locality'] + '"', end=' ')
            result = geocoder.osm(a['locality']).json
            success = result['status'] == 'OK' and result['country'] == 'Italia'

        if success:
            if verbose:
                print('OK!')
            x['coords'] = result['geometry']['coordinates']
            x['address'] = address
            webSite = s['contacts']['contact']['primary']['webSite']
            if webSite:
                x['webSite'] = webSite
            suppliers_out.append(x)
    return suppliers_out


def update_geo_db(verbose=False):
    with pymongo.connection.Connection() as conn:
        coll = conn['sbcatalog']['geosupplier']
        coll.drop()
        coll.insert(get_addresses(verbose))


def get_addresses_json():
    return json.dumps(get_addresses())
