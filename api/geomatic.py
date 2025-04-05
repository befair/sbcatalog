import time
from geopy.geocoders import Nominatim
import geocoder
import json
from pymongo import MongoClient

from settings import MONGO_HOST, MONGO_PORT


def get_addresses(verbose=False):
    geolocator = Nominatim(user_agent="SBCatalog/0.9 (dev@befair.it)")
    with MongoClient(MONGO_HOST, MONGO_PORT) as client:
        coll = client['sbcatalog']['supplier']
        suppliers_in = coll.find()

        suppliers_out = []
        for c, s in enumerate(suppliers_in):
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
                print('Trying full address: "' + address + '"', end='\n')

            try:
                # Try full address first.
                location = geolocator.geocode(address)
                if location is None:
                    # If not successful, try using only the locality.
                    if a.get('locality'):
                        if verbose:
                            print('NOT FOUND! Trying locality: "' + a.get('locality') + '"', end=' ')
                        location = geolocator.geocode(a.get('locality'))

                if location is not None:
                    if verbose:
                        print('OK!')
                    # Get coordinates from the result.
                    x['coords'] = (location.longitude, location.latitude)
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
            except Exception as e:
                print(f"ERROR {c=}: {e}")
                if c >= 10:
                    break
            time.sleep(1.2)
                
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
