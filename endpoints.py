
from eve.endpoints import collections_endpoint, _resource
from eve.utils import request_method
from eve.methods import post
from eve.render import send_response

from flask import request

def xml_collections_endpoint(**lookup):

    resource = _resource()
    response = None
    method = request_method()
    if request.content_type.endswith("/xml"):
        if method == "POST":
            #TODO: translate xml to json
            response = post(resource, payl=[{"name": "MINO", "lastname": "REITANO"}])
        else:
            raise NotImplementedError("Other methods not implemented. PROBLEM: GET already implemented")
        return send_response(resource, response)

    else:
        rv = collections_endpoint(**lookup)
    return rv
