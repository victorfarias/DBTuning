import os

from subprocess import call
from ..utils.ContextManager import cd
from ..utils import paths



class OLTPBenchmark(object):

    def __init__(self):
        pass
    
    def load(self, db, config_path):
        with cd(paths.OLTP_BIN_DIR):
            call(["./oltpbenchmark", "-b", db, "-c", config_path, "--create=true", "--load=true"])
