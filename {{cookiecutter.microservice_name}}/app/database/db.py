# Database connection
import couchdb
import aerospike


class CoucheDB:
    def __init__(self, db):
        self.db = db

    def connect(self):
        couch = couchdb.Server('http://admin:password@localhost:5984/')
        db = couch[self.db]
        return db


class AerospikeDb:
    def __init__(self, host):
        self.config = {
            'hosts': [
                ('127.0.0.1', 3000)
            ],
            'policies': {
                'timeout': 1000  # milliseconds
            }
        }

    def get_connection(self):
        client = aerospike.client(self.config)
        client.connect()
        return client
