# -*- encoding: utf-8 -*-
# This file is part of sbcatalog
#
# sbcatalog is Copyright © 2015 beFair.it
#
# This program is free software: you can redistribute it and/or modify it under
# the terms of the GNU Affero General Public License version 3, as published by
# the Free Software Foundation.
#
# This program is distributed in the hope that it will be useful, but WITHOUT
# ANY WARRANTY; without even the implied warranties of MERCHANTABILITY,
# SATISFACTORY QUALITY, or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

"""
Driver to serialize xml into json.

Encapsulation here make it able to be developed
in other ways in future...
"""

import xmltodict
# other package = xml2dict
# import decoder
# xmltodict = XML2Dict()

import sys
from collections import OrderedDict


def xml2json(xmlstring):
    """
    Convert to python dict (i.e: quite-a-json ;))

    - Strip the root element
    - Move the root attributes to each element of the collection
    """
    # print(xmlstring)
    d = list(xmltodict.parse(xmlstring).values())[0]

    # remove root element and take away root attributes
    root_attrs = {}
    for k, v in d.items():
        if k.startswith('@'):
            root_attrs[k] = d.pop(k)

    # Append root_attrs to each top-level element
    tle = list(d.values())
    try:
        tle = tle[0]
    except:
        pass

    for v in tle:
        if isinstance(v, str):
            v = OrderedDict({'#text': v})
        v.update(root_attrs)

    rv = list(d.values())[0]
    if not isinstance(rv, list):
        rv = [rv]

    return rv

if __name__ == "__main__":
    try:
        xmlstring = sys.argv[1]
    except IndexError:
        xmlstring = sys.stdin.read()

    from pprint import pprint
    import json
    pprint(json.loads(
        json.dumps(xml2json(xmlstring))
    ))
