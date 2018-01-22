import urllib
import os
import sh


MEMSQL_URL = "http://download.memsql.com/memsql-ops-6.0.8/memsql-ops-6.0.8.tar.gz"



def install():
    bin_dir = os.path.dirname(__file__) +'/../bin'
    bin_path = bin_dir +"/"+ "memsql.tar.gz"
    bin_name = os.path.basename(MEMSQL_URL);

    if not os.path.exists(bin_dir):
        os.makedirs(bin_dir)

    if os.path.isfile(bin_path): 
        print "Binaries already downloaded"
    else:        
        print "Downloading MemSQl Binaries"
        urllib.urlretrieve (MEMSQL_URL, bin_path)

    sh.tar("zxvf", bin_path, '-C', bin_dir)

    ops_path = bin_dir + "/"+ bin_name[:-7] + "/memsql-ops/memsql-ops"
    ops = sh.Command(ops_path)
    for line in ops("start", _err_to_out=True, _iter=True, _out_bufsize=1000):
        print line

    print
    print "Follow to http://localhost:9000 to complete installation"

if __name__ == "__main__":
    install()

      