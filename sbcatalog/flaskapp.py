from eve import Eve
from endpoints import xml_collections_endpoint


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
        self.view_functions[endpoint] = xml_collections_endpoint
        settings = self.config['DOMAIN'][resource]
        self.add_url_rule(self.api_prefix + '/gdxp/supplier',
                          endpoint,
                          view_func=xml_collections_endpoint,
                          methods=settings['resource_methods'] + ['OPTIONS'])

        # MIGHT BE USEFUL
        # url = '%s/%s' % (self.api_prefix, settings['url'])
        # self.add_url_rule(url, endpoint, view_func=gdxp_collections_endpoint,
        #    methods=settings['resource_methods'] + ['OPTIONS'])
