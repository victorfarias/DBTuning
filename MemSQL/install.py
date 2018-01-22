import urllib
import os
import sh


MEMSQL_URL = "http://download.memsql.com/memsql-ops-6.0.8/memsql-ops-6.0.8.tar.gz"
BIN_DIR = os.path.dirname(__file__) +'/../bin'
BIN_PATH = BIN_DIR +"/"+ "memsql.tar.gz"
BIN_NAME = os.path.basename(MEMSQL_URL);


if __name__ == "__main__":
    if not os.path.exists(BIN_DIR):
        os.makedirs(BIN_DIR)

    if os.path.isfile(BIN_PATH): 
        print 'Binaries already downloaded'
    else:        
        print 'Downloading MemSQl Binaries'
        urllib.urlretrieve (MEMSQL_URL, BIN_PATH)

    sh.tar('zxvf', BIN_PATH, '-C', BIN_DIR)
    