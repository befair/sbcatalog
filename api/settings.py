import os


# General settings
ENV = os.getenv('APP_ENV', 'dev')

if ENV == 'dev':
    DEBUG = True
    MONGO_SOCKET_TIMEOUT_MS = 60 * 1000
    MONGO_CONNECT_TIMEOUT_MS = 60 * 1000
else:
    DEBUG = False

# Let's just use the local mongod instance. Edit as needed.

# Please note that MONGO_HOST and MONGO_PORT could very well be left
# out as they already default to a bare bones local 'mongod' instance.
MONGO_HOST = os.getenv('MONGO_HOST', 'db')
MONGO_PORT = os.getenv('MONGO_PORT', 27017)
MONGO_USERNAME = os.getenv('MONGO_USERNAME', '')
MONGO_PASSWORD = os.getenv('MONGO_PASSWORD', '')
MONGO_DBNAME = os.getenv('MONGO_DBNAME', 'sbcatalog')

# API Namespacing
URL_PREFIX = 'api'
API_VERSION = 'v1'

# GET Request will return all the results instead of a restricted set
PAGINATION = False

# Enable reads (GET), inserts (POST) and DELETE for resources/collections
# (if you omit this line, the API will default to ['GET'] and provide
# read-only access to the endpoint).
RESOURCE_METHODS = ['GET', 'POST', 'DELETE']

# Enable reads (GET), edits (PATCH), replacements (PUT) and deletes of
# individual items  (defaults to read-only item access).
ITEM_METHODS = ['GET', 'PATCH', 'PUT', 'DELETE']

geosupplier_schema = {
    'name': {
        'type': 'string',
        'minlength': 1,
        'maxlength': 40,
    },
    'address': {
        'type': 'string',
        'minlength': 1,
        'maxlength': 40,
    },
    'webSite': {
        'type': 'string',
        'minlength': 1,
        'maxlength': 40,
    },
    'coords': {
        'type': 'list',
        'items': {
            'type': 'float',
            'type': 'float'
        }
    }
}

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
    'note': {
        'type': 'string',
        'minlength': 1,
        'maxlength': 20,
    },
    'extraFields': {
        'type': 'dict',
        'schema': {
            'extraField': {
                'type': 'string',
                'minlength': 1,
                'maxlength': 20,
            }
        }
    },
    'address': {
        'type': 'dict',
        'schema': {
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
        'schema': {
            'contact': {
                'type': 'dict',
                'schema': {
                    'primary': {
                        'type': 'dict',
                        'schema': {
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
                    'extraContact': {
                        'type': 'dict',
                        'schema': {
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
    'logo': {
        'type': 'string',
        'minlength': 1,
    },
    'products': {
        'type': 'dict',
        'schema': {
            'product': {
                'type': 'dict',
                'schema': {
                    'sku': {
                        'type': 'string',
                        'minlength': 1,
                        'maxlength': 15,
                    },
                    'name': {
                        'type': 'string',
                        'minlength': 1,
                        'maxlength': 15,
                    },
                    'category': {
                        'type': 'string',
                        'minlength': 1,
                        'maxlength': 15,
                    },
                    'um': {
                        'type': 'string',
                        'minlength': 1,
                        'maxlength': 15,
                    },
                    'description': {
                        'type': 'string',
                        'minlength': 1,
                        'maxlength': 15,
                    },
                    'orderInfo': {
                        'type': 'dict',
                        'schema': {
                            'packageQty': {
                                'type': 'string',
                                'minlength': 1,
                                'maxlength': 15,
                            },
                            'minQty': {
                                'type': 'string',
                                'minlength': 1,
                                'maxlength': 15,
                            },
                            'mulQty': {
                                'type': 'string',
                                'minlength': 1,
                                'maxlength': 15,
                            },
                            'maxQty': {
                                'type': 'string',
                                'minlength': 1,
                                'maxlength': 15,
                            },
                            'umPrice': {
                                'type': 'string',
                                'minlength': 1,
                                'maxlength': 15,
                            },
                            'shippingCost': {
                                'type': 'string',
                                'minlength': 1,
                                'maxlength': 15,
                            }
                        }
                    },
                    'variants': {
                        'type': 'dict',
                        'schema': {
                            'extraFields': {
                                'type': 'dict',
                                'schema': {
                                    'extraField': {
                                        'type': 'string',
                                        'minlength': 1,
                                        'maxlength': 20,
                                    }
                                }
                            }
                        }
                    }
                }
            }
        }
    },
}

supplier = {
    # 'title' tag used in item links. Defaults to the resource title minus
    # the final, plural 's' (works fine in most cases but not for 'people')
    # 'item_title': 'person',

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

geosupplier = {
    # most global settings can be overridden at resource level
    'resource_methods': ['GET'],
    'schema': geosupplier_schema
}

DOMAIN = {'supplier': supplier, 'geosupplier': geosupplier}
