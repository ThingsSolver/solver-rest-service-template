# Database access object
# Here we work with db object but business logic should be in services.py
from app.database.db import CoucheDB
from app.database.db import AerospikeDb
from aerospike import predicates as p


userInfoDB = CoucheDB('user-info')


class CouchDbQuery:
    @staticmethod
    def query_user_info_from_cdb(uid):
        return userInfoDB.connect()[uid]


class AerospikeQuery:
    def __init__(self):
        self.c = AerospikeDb('localhost').get_connection()

    def get_record(self, db_set, uid):
        (key, meta, bins) = self.c.get(('test', db_set, uid))
        return bins

    def get_fields_in_record(self, db_set,  uid, attributes):
        is_tuple = type(attributes) is tuple
        if not is_tuple:
            raise TypeError
        (key, meta, bins) = self.c.select(('test', db_set, uid), attributes)
        return bins

    def query(self, db_set, uid):
        query = self.c.query('test', db_set)
        query.where(p.equals('id', uid))
        res = {}
        for record in query.results():
            ns, sets, bins = record
            res.update(bins)
        return res
