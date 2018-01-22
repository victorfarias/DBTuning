import sh

MEMSQL_URL = "http://download.memsql.com/memsql-ops-6.0.8/memsql-ops-6.0.8.tar.gz"
BIN_DIR = os.path.dirname(__file__) +'/../bin'
BIN_NAME = os.path.basename(MEMSQL_URL);
OPS_PATH = BIN_DIR + "/"+ BIN_NAME[:-7] + "/memsql-ops/memsql-ops"

class MemSQLAdmin(object):

    def __init__(self):
        ops_path = bin_dir + "/"+ bin_name[:-7] + "/memsql-ops/memsql-ops"
        self.ops = sh.Command(ops_path)
        self.ops_
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
        for line in ops("start", _err_to_out=True, _iter=True, _out_bufsize=1000):
            print line

    def stop(self):
        for line in ops("stop", _err_to_out=True, _iter=True, _out_bufsize=1000):
            print line

    def set_param(key, value):
        pass        




    
