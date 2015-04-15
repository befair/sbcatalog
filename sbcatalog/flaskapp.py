from eve import Eve
from endpoints import xml_collections_endpoint

class XMLEve(Eve):
    """
    This class aims to let Eve be able to import XML documents
    
    It is meant to overload the view function `collections endpoint`. 
    It interprets the text/xml Content-Type and call the `post` function
        with the forged json payload.
    """

    def __init__(self, *args, **kw):
        """
        Init Eve and oveload enpoints view_functions.
        """
        super(XMLEve, self).__init__(*args, **kw)

        # TODO: iterate over all resources

        resource = 'supplier'
        endpoint = resource + "|resource"
        self.view_functions[endpoint] = xml_collections_endpoint

        # MAY BE USEFUL
        #settings = self.config['DOMAIN'][resource]
        #url = '%s/%s' % (self.api_prefix, settings['url'])                                                                             
        #self.add_url_rule(url, endpoint, view_func=gdxp_collections_endpoint,
        #    methods=settings['resource_methods'] + ['OPTIONS'])

