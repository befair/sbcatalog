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

from eve.endpoints import collections_endpoint, _resource
from eve.utils import request_method, config
from eve.methods.post import post_internal
from eve.render import send_response

from flask import request
from utils import crossdomain

import json
import xmltodict
from xml2json import xml2json


def popper(d):
    for k in [config.ID_FIELD, config.LAST_UPDATED, config.DATE_CREATED,
              config.ETAG, config.ISSUES, config.STATUS, config.LINKS]:
        d.pop(k, None)
    return d


@crossdomain(origin='*')
def xml_collections_endpoint(**lookup):
    resource = _resource()
    response = None
    method = request_method()
    if request.content_type.endswith("/xml"):
        if method == "POST":
            # response = post(resource, payl=xml2json(request.data))
            response = post_internal(resource,
                                     payl=xml2json(request.data),
                                     skip_validation=True)
        elif method == "GET":
            response = collections_endpoint(**lookup)
            l = json.loads(response.data.decode('utf-8'))['_items']
            response.data = xmltodict.unparse({
                'gdxp': {
                    "supplier": list(map(popper, l))
                }
            })
        else:
            raise NotImplementedError('Not implemented')

        return send_response(resource, response)

    else:
        return collections_endpoint(**lookup)


@crossdomain(origin='*')
def geo_collections_endpoint(**lookup):
    resource = _resource()
    response = collections_endpoint(**lookup)
    return send_response(resource, response)
