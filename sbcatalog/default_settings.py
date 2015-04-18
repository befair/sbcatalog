
# Let's just use the local mongod instance. Edit as needed.

# Please note that MONGO_HOST and MONGO_PORT could very well be left
# out as they already default to a bare bones local 'mongod' instance.
MONGO_HOST = 'localhost'
MONGO_PORT = 27017
MONGO_USERNAME = ''
MONGO_PASSWORD = ''
MONGO_DBNAME = 'sbcatalog'

# Enable reads (GET), inserts (POST) and DELETE for resources/collections
# (if you omit this line, the API will default to ['GET'] and provide
# read-only access to the endpoint).
RESOURCE_METHODS = ['GET', 'POST', 'DELETE']

# Enable reads (GET), edits (PATCH), replacements (PUT) and deletes of
# individual items  (defaults to read-only item access).
ITEM_METHODS = ['GET', 'PATCH', 'PUT', 'DELETE']

schema = {
    # Schema definition, based on Cerberus grammar. Check the Cerberus project
    # (https://github.com/nicolaiarocci/cerberus) for details.
    'name': {
        'type': 'string',
        'minlength': 1,
        'maxlength': 10,
    },
    'taxCode': {
        'type': 'string',
        'minlength': 1,
        'maxlength': 20,
    },
    'vatNumber': {
        'type': 'string',
        'minlength': 1,
        'maxlength': 20,
    },
    'address': {
        'type': 'dict',
        'schema' : {
            'street': {
                'type': 'string',
                'minlength': 1,
                'maxlength': 20,
            },
            'locality': {
                'type': 'string',
                'minlength': 1,
                'maxlength': 20,
            },
            'zipcode': {
                'type': 'string',
                'minlength': 1,
                'maxlength': 20,
            },
            'country': {
                'type': 'string',
                'minlength': 1,
                'maxlength': 20,
            }
        }
    },
    'contacts': {
        'type': 'dict',
        'schema' : {
    'contact' : {
        'type': 'dict',
        'schema' : {
            'primary' : {
                'type' : 'dict',
                'schema' : {
                    'phoneNumber': {
                        'type': 'string',
                        'minlength': 1,
                        'maxlength': 20,
                    },
                    'faxNumber': {
                        'type': 'string',
                        'minlength': 1,
                        'maxlength': 20,
                    },
                    'emailAddress': {
                        'type': 'string',
                        'minlength': 1,
                        'maxlength': 20,
                    },
                    'webSite': {
                        'type': 'string',
                        'minlength': 1,
                        'maxlength': 20,
                    }
                }
            },
            'extraContact' : {
                'type' : 'dict',
                'schema' : {
                    'firstName': {
                        'type': 'string',
                        'minlength': 1,
                        'maxlength': 20,
                    },
                    'lastName': {
                        'type': 'string',
                        'minlength': 1,
                        'maxlength': 20,
                    },
                    'phoneNumber': {
                        'type': 'string',
                        'minlength': 1,
                        'maxlength': 20,
                    },
                    'mobileNumber': {
                        'type': 'string',
                        'minlength': 1,
                        'maxlength': 20,
                    },
                    'faxNumber': {
                        'type': 'string',
                        'minlength': 1,
                        'maxlength': 20,
                    },
                    'emailAddress': {
                        'type': 'string',
                        'minlength': 1,
                        'maxlength': 20,
                    }
                }
            }
        }
    }
    }
    },
    #'products': {
    #    'type': 'dict',
    #    'schema' : {
    #'product' : {
    #    'type': 'dict',
    #    'schema' : {
    #        'sku' : {
    #            'type': 'string',
    #            'minlength': 1,
    #            'maxlength': 15,
    #        },
    #        'name' : {
    #            'type': 'string',
    #            'minlength': 1,
    #            'maxlength': 15,
    #        },
    #        'category' : {
    #            'type': 'string',
    #            'minlength': 1,
    #            'maxlength': 15,
    #        },
    #        'um' : {
    #            'type': 'string',
    #            'minlength': 1,
    #            'maxlength': 15,
    #        },
    #        'description' : {
    #            'type': 'string',
    #            'minlength': 1,
    #            'maxlength': 15,
    #        },
    #        'orderInfo' : {
    #            'type' : 'dict',
    #            'schema': {
    #                'packageQty' : {
    #                    'type': 'string',
    #                    'minlength': 1,
    #                    'maxlength': 15,
    #                },
    #                'minQty' : {
    #                    'type': 'string',
    #                    'minlength': 1,
    #                    'maxlength': 15,
    #                },
    #                'mulQty' : {
    #                    'type': 'string',
    #                    'minlength': 1,
    #                    'maxlength': 15,
    #                },
    #                'maxQty' : {
    #                    'type': 'string',
    #                    'minlength': 1,
    #                    'maxlength': 15,
    #                },
    #                'umPrice' : {
    #                    'type': 'string',
    #                    'minlength': 1,
    #                    'maxlength': 15,
    #                },
    #                'shippingCost' : {
    #                    'type': 'string',
    #                    'minlength': 1,
    #                    'maxlength': 15,
    #                }
    #            }
    #        },
    #        #'variants' : {
    #        #    'type' : 'dict',
    #        #    'schema' : {
    #        #        'extraFields' : {
    #        #            'type' : 'dict',
    #        #            'schema' : {
    #        #                'extraField': {
    #        #                    'type': 'string',
    #        #                    'minlength': 1,
    #        #                    'maxlength': 20,
    #        #                }
    #        #            }
    #        #        }
    #        #    }
    #        #}
    #    }
    #}
    #}
    #},
    'lastname': {
        'type': 'string',
        'minlength': 1,
        'maxlength': 15,
        'required': True,
        # talk about hard constraints! For the purpose of the demo
        # 'lastname' is an API entry-point, so we need it to be unique.
        'unique': True,
    },
    # 'role' is a list, and can only contain values from 'allowed'.
    'role': {
        'type': 'list',
        'allowed': ["author", "contributor", "copy"],
    },
    # An embedded 'strongly-typed' dictionary.
    'location': {
        'type': 'dict',
        'schema': {
            'address': {'type': 'string'},
            'city': {'type': 'string'}
        },
    },
    'born': {
        'type': 'datetime',
    },
}

supplier = {
    # 'title' tag used in item links. Defaults to the resource title minus
    # the final, plural 's' (works fine in most cases but not for 'people')
    #'item_title': 'person',

    # by default the standard item entry point is defined as
    # '/people/<ObjectId>'. We leave it untouched, and we also enable an
    # additional read-only entry point. This way consumers can also perform
    # GET requests at '/people/<lastname>'.
    'additional_lookup': {
        'url': 'regex("[\w]+")',
        'field': 'name'
    },

    # We choose to override global cache-control directives for this resource.
    'cache_control': 'max-age=10,must-revalidate',
    'cache_expires': 10,

    # most global settings can be overridden at resource level
    'resource_methods': ['GET', 'POST'],

    'schema': schema
}


DOMAIN = { 'supplier': supplier }
