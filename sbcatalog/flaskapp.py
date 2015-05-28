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

from eve import Eve
from endpoints import xml_collections_endpoint, geo_collections_endpoint


class XMLEve(Eve):
    """
    This class aims to let Eve be able to import XML documents

    It is meant to overload the view function `collections endpoint`.
    It interprets the text/xml Content-Type and calls the `post` function
    with the forged json payload.
    """

    def __init__(self, *args, **kw):
        """
        Init Eve and overload enpoints view_functions.
        """
        super(XMLEve, self).__init__(*args, **kw)

        # TODO: iterate over all resources

        resource = 'supplier'
        endpoint = resource + "|resource"
        geo_resource = 'geosupplier'
        geo_endpoint = geo_resource + "|resource"
        self.view_functions[endpoint] = xml_collections_endpoint
        self.view_functions[geo_endpoint] = geo_collections_endpoint
        settings = self.config['DOMAIN'][resource]
        geo_settings = self.config['DOMAIN'][geo_resource]
        self.add_url_rule(self.api_prefix + '/gdxp/supplier',
                          endpoint,
                          view_func=xml_collections_endpoint,
                          methods=settings['resource_methods'] + ['OPTIONS'])
        self.add_url_rule(self.api_prefix + '/geo/supplier',
                          geo_endpoint,
                          view_func=geo_collections_endpoint,
                          methods=geo_settings['resource_methods'] + ['OPTIONS'])

        # MIGHT BE USEFUL
        # url = '%s/%s' % (self.api_prefix, settings['url'])
        # self.add_url_rule(url, endpoint, view_func=gdxp_collections_endpoint,
        #    methods=settings['resource_methods'] + ['OPTIONS'])
