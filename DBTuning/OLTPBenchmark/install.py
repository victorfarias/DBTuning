import os

from subprocess import call
from ..utils import paths

def install():
    print
    print "Getting OLTPBenchmark"
    call(["git", "clone", "https://github.com/victorfarias/oltpbench.git", paths.OLTP_BIN_DIR])

    os.chdir(paths.OLTP_BIN_DIR)

    print
    print "Building OLPTBenchmark"
    call(["ant"])

    print
    print "OLTPBenchmark installed"

if __name__ == "__main__":
    install()