
from eve.endpoints import collections_endpoint, _resource
from eve.utils import request_method
from eve.methods import post
from eve.render import send_response

from flask import request

from xml2json import xml2json

def xml_collections_endpoint(**lookup):

    resource = _resource()
    response = None
    method = request_method()
    if request.content_type.endswith("/xml"):
        if method == "POST":
            response = post(resource, payl=xml2json(request.data))
        else:
            raise NotImplementedError(
                "Other methods not implemented."
                "PROBLEM: GET already implemented... use gdxp/xml?!?"
            )
        return send_response(resource, response)

    else:
        rv = collections_endpoint(**lookup)
    return rv
