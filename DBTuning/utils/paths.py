import os

MEMSQL_URL = "http://download.memsql.com/memsql-ops-6.0.8/memsql-ops-6.0.8.tar.gz"
MEMSQL_BIN_URL = "http://download.memsql.com/releases/latest/memsqlbin_amd64.tar.gz"

THIS_DIR = os.path.dirname(__file__)
BIN_DIR = THIS_DIR + "/../../bin"

OLTP_BIN_DIR = BIN_DIR + "/oltpbench"

MEM_DIR = os.path.basename(MEMSQL_URL)
MEM_TAR = BIN_DIR +"/"+ "memsql.tar.gz"
OPS_PATH = BIN_DIR + "/"+ MEM_DIR[:-7] + "/memsql-ops/memsql-ops"