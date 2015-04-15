"""
Driver to serialize xml into json.

Encapsulation here make it able to be developed
in other ways in future...
"""

import xmltodict
# other package = xml2dict
# import decoder 
# xmltodict = XML2Dict()

import sys, types
from collections import OrderedDict

def xml2json(xmlstring):
    """
    Convert to python dict (i.e: quite-a-json ;))

    - Strip the root element
    - Move the root attributes to each element of the collection
    """
    print xmlstring
    d = xmltodict.parse(xmlstring).values()[0]
    print d

    # remove root element and take away root attributes
    root_attrs = {}
    for k,v in d.items():
        if k.startswith('@'):
            root_attrs[k] = d.pop(k)

    # Append root_attrs to each top-level element
    tle = d.values()
    if isinstance(tle, list):
        tle = tle[0]

    for v in tle:
        if isinstance(v, types.StringTypes):
            v = OrderedDict({'#text': v})
        print(v)
        v.update(root_attrs)

    return d

if __name__ == "__main__":
    try:
        xmlstring = sys.argv[1]
    except IndexError:
        xmlstring = sys.stdin.read()

    from pprint import pprint
    pprint(xml2json(xmlstring))

