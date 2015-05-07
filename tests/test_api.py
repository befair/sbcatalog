from http import client
import xmltodict, json, codecs

conn = client.HTTPConnection('localhost', 5000)
supplier_file = 'test_data.gdxp'

def assertCode(response, expected_code=200):
    """ Assert that response code is the expected """
    assert response.code == expected_code, 'Good response code'

def test_post_gdxp():
    """ POST test for importing gdxp suppliers data """
    try:
        with codecs.open(supplier_file, 'r', 'utf-8') as f:
            xml = f.read().encode('utf-8')
    except IOError:
        assert False, "%s not found" % supplier_file
    conn.request('POST', '/gdxp/supplier', xml, {'Content-type': 'text/xml'})
    r = conn.getresponse()
    assertCode(r, 201)


def test_get_json():
    """ GET test for exporting suppliers data in json format """
    conn.request('GET','/supplier')
    r = conn.getresponse()
    assertCode(r)
    data = r.read().decode('utf_8')
    assert '"name": "Acquaterra"' in data
    assert isinstance(json.loads(data), dict), \
        'Response data is a JSON string'
    
def test_get_gdxp():
    """ GET test for exporting suppliers data in gxdp format """
    conn.request('GET', '/gdxp/supplier/', headers = {'Content-type': 'text/xml'})
    r = conn.getresponse()
    assertCode(r)
    data = r.read().decode('utf-8')
    assert '<name>Acquaterra</name>' in data
    assert isinstance(xmltodict.parse(data), dict)
