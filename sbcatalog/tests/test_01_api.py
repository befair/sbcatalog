from http import client
import sbcatalog.geomatic
import xmltodict
import json
import codecs

# Settings

conn = client.HTTPConnection('localhost', 5000)
supplier_file = 'test_data.gdxp'

# Utilities


def assertCode(response, expected_code=200):
    """ Assert that response code is the expected """
    assert response.code == expected_code, "Response code is excepted"


def elaborate_response():
    """ Check return code of response and return DATA """
    r = conn.getresponse()
    assertCode(r)
    return r.read().decode('utf_8')


def elaborate_response_json():
    """ Same as elaborate_response() but return JSON data """
    data = json.loads(elaborate_response())
    assert isinstance(data, dict), "Data is a JSON string"
    return data


def get_item(data):
    """ Check _items type and return 1st item in the list """
    items = data['_items']
    item = items[0]
    # check types
    assert isinstance(items, list)
    assert isinstance(item, dict)
    return item


def check_supplier(supplier):
    """ Check the supplier according to test data """
    assert supplier['name'] == "Acquaterra"
    assert supplier['address']['street'] == "Loc. campochiesa, 6"
    assert supplier['address']['locality'] == "Matelica"
    assert supplier['address']['zipcode'] == "62024"

# Tests


def test_01_post_gdxp():
    """ POST test for importing gdxp suppliers data """
    try:
        with codecs.open(supplier_file, 'r', 'utf-8') as f:
            xml = f.read().encode('utf-8')
    except IOError:
        assert False, "%s not found" % supplier_file
    conn.request('POST', '/gdxp/supplier', xml, {'Content-type': 'text/xml'})
    r = conn.getresponse()
    assertCode(r, 201)


def test_02_get_json():
    """ GET test for exporting suppliers data in json format """
    # test GET /supplier
    conn.request('GET', '/supplier')
    data = elaborate_response_json()

    # check supplier data
    item = get_item(data)
    check_supplier(item)


def test_03_get_gdxp():
    """ GET test for exporting suppliers data in gxdp format """
    # test GET /gdxp/supplier
    conn.request('GET', '/gdxp/supplier/', headers={'Content-type': 'text/xml'})
    data = elaborate_response()

    # check supplier data
    item = xmltodict.parse(data)['gdxp']['supplier'][0]
    check_supplier(item)


def test_04_geo_api():
    """ Data generation and GET test for geo API """
    # test geodb generation
    sbcatalog.geomatic.update_geo_db()

    # test GET /geo/supplier
    conn.request('GET', '/geo/supplier')
    data = elaborate_response_json()
    item = get_item(data)

    # check data
    assert item['address'] == "Matelica 62024 Loc. campochiesa, 6"
    # assert item['webSite'] == "http://www.cantinaprimadiesanatoglia.it/"
    assert item['name'] == "Acquaterra"
    assert item['coords'] == [13.00948, 43.2565867]
