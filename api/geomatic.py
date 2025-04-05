import geocoder
import json
from pymongo import MongoClient
from settings import MONGO_HOST, MONGO_PORT

def get_addresses(verbose=False):
    with MongoClient(MONGO_HOST, MONGO_PORT) as client:
        coll = client['sbcatalog']['supplier']
        suppliers_in = coll.find()

        suppliers_out = []
        for s in suppliers_in:
            success = False
            x = {}
            x['name'] = s.get('name')
            a = s.get('address', {})
            # Build the address string from parts if available.
            address_parts = []
            for k in ['locality', 'zipcode', 'street']:
                if a.get(k):
                    address_parts.append(a[k])
            address = " ".join(address_parts)
            if verbose:
                print('Trying full address: "' + address + '"', end=' ')
            # Try full address first.
            result = geocoder.osm(address)
            result_json = result.json
            if result_json.get('status') == 'OK' and result_json.get('country') == 'Italia':
                success = True
            # If not successful, try using only the locality.
            elif a.get('locality'):
                if verbose:
                    print('NOT FOUND! Trying locality: "' + a.get('locality') + '"', end=' ')
                result = geocoder.osm(a.get('locality'))
                result_json = result.json
                success = result_json.get('status') == 'OK' and result_json.get('country') == 'Italia'

            if success:
                if verbose:
                    print('OK!')
                # Get coordinates from the result.
                geometry = result_json.get('geometry', {})
                x['coords'] = geometry.get('coordinates')
                x['address'] = address
                # Extract webSite from nested contacts.
                webSite = (
                    s.get('contacts', {})
                     .get('contact', {})
                     .get('primary', {})
                     .get('webSite')
                )
                if webSite:
                    x['webSite'] = webSite
                suppliers_out.append(x)
            else:
                if verbose:
                    print('FAILED!')
    return suppliers_out

def update_geo_db(verbose=False):
    with MongoClient(MONGO_HOST, MONGO_PORT) as client:
        coll = client['sbcatalog']['geosupplier']
        # Drop the collection before updating.
        coll.drop()
        addresses = get_addresses(verbose)
        # Use insert_many to insert multiple documents.
        if addresses:
            coll.insert_many(addresses)

def get_addresses_json():
    return json.dumps(get_addresses())

if __name__ == '__main__':
    # Example usage: update the geosupplier collection and print addresses as JSON.
    update_geo_db(verbose=True)
    print(get_addresses_json())
