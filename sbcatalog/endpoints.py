from eve.endpoints import collections_endpoint, _resource
from eve.utils import request_method, config
from eve.methods import post
from eve.methods.post import post_internal
from eve.render import send_response

from flask import request
from utils import crossdomain

import json
import xmltodict
from xml2json import xml2json

def popper(d):
    for k in [config.ID_FIELD, config.LAST_UPDATED, config.DATE_CREATED,
            config.ETAG, config.ISSUES, config.STATUS, config.LINKS] :
        d.pop(k, None)
    return d

@crossdomain(origin='*')
def xml_collections_endpoint(**lookup):

    resource = _resource()
    response = None
    method = request_method()
    if request.content_type.endswith("/xml"):
        if method == "POST":
            #response = post(resource, payl=xml2json(request.data))
            response = post_internal(resource, payl=xml2json(request.data), skip_validation=True)
        elif method == "GET":
            response = collections_endpoint(**lookup)
            l = json.loads(response.data)['_items']
            response.data = xmltodict.unparse({
                'gdxp' : {
                    "supplier": map(popper, l)
                }
            })
        else:
            raise NotImplementedError('Not implemented')

        return send_response(resource, response)

    else:
        return collections_endpoint(**lookup)
