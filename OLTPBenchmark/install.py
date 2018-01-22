import os

from subprocess import call

OLTPBENCH_DIR = os.path.dirname(__file__) +'/../bin/oltpbench'

def install():
    print
    print "Getting OLTPBenchmark"
    call(["git", "clone", "https://github.com/oltpbenchmark/oltpbench.git", OLTPBENCH_DIR])

    os.chdir(OLTPBENCH_DIR)

    print
    print "Building OLPTBenchmark"
    call(["ant"])

    print
    print "OLTPBenchmark installed"


if __name__ == "__main__":
    install()

