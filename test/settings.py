import os


MONGO_HOST = os.getenv('MONGO_HOST', 'db')
MONGO_PORT = os.getenv('MONGO_PORT', 27017)
MONGO_USERNAME = os.getenv('MONGO_USERNAME', '')
MONGO_PASSWORD = os.getenv('MONGO_PASSWORD', '')
MONGO_DBNAME = os.getenv('MONGO_DBNAME', 'sbcatalog')

NGINX_HOST = os.getenv('NGINX_HOST', 'proxy')
NGINX_PORT = os.getenv('NGINX_PORT', '80')

ROOT = os.getenv('ROOT', '/code')
SUPPLIER_FILE = ROOT + '/test/fixtures/data.gdxp'
