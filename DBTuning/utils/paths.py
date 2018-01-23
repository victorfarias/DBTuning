import os

MEMSQL_URL = "http://download.memsql.com/memsql-ops-6.0.8/memsql-ops-6.0.8.tar.gz"

THIS_DIR = os.path.dirname(__file__)
BIN_DIR = THIS_DIR + "/../../bin"

OLTP_BIN_DIR = BIN_DIR + "/oltpbench"

MEM_DIR = os.path.basename(MEMSQL_URL);
OPS_PATH = BIN_DIR + "/"+ MEM_DIR[:-7] + "/memsql-ops/memsql-ops"

