import sh

from subprocess import call
from ..utils import paths

class MemSQLAdmin(object):

    def __init__(self):
        self.params = ["load_data_read_size", 
                        "load_data_write_size",
                        "lock_wait_timeout",
                        "max_prepared_stmt_count",
                        "multi_insert_tuple_count",
                        "net_read_timeout",
                        "net_write_timeout",
                        "plan_expiration_minutes",
                        "query_parallelism",
                        "transaction_buffer"]

    def start(self):
        call([paths.OPS_PATH, "start"])
        
    def stop(self):
        call([paths.OPS_PATH, "stop"])

    def set_param(key, value):
        pass        




    
