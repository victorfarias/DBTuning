import urllib
import os
from subprocess import call

from ..utils import paths


def install():
    
    if not os.path.exists(paths.BIN_DIR):
        os.makedirs(paths.BIN_DIR)

    if os.path.isfile(paths.MEM_TAR): 
        print "Binaries already downloaded"
    else:        
        print "Downloading MemSQl Binaries"
        urllib.urlretrieve (paths.MEMSQL_URL, paths.MEM_TAR)

    call(["tar","zxvf", paths.MEM_TAR, '-C', paths.BIN_DIR])
    
    call([paths.OPS_PATH,"start"])    

    print
    print "Follow to http://localhost:9000 to complete installation"

def uninstall():
    pass
    

if __name__ == "__main__":
    install()

      