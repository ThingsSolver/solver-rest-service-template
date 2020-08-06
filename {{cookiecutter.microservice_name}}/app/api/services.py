# Business logic, please delete example
from app.database.daos import AerospikeQuery


class Basic:
    def __init__(self):
        self.c = AerospikeQuery()

    def get_first_purchase(self, uid, location, address):
        pass

    def get_latest_purchase(self, uid, location, address):
        pass

    def get_activation_datetime(self, uid, location, address):
        pass

    def get_best_basket(self, uid, location, address, dt_from, dt_to):
        pass

    def get_customer_info(self, uid):
        return self.c.get_record(uid=uid, db_set='CustomerInfo')

