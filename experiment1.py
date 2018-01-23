import os

from DBTuning.OLTPBenchmark.api import OLTPBenchmark
from DBTuning.MemSQL.api import MemSQLAdmin

def run():

    # mem_admin = MemSQLAdmin()
    # mem_admin.start()

    oltp = OLTPBenchmark()
    oltp.load("wikipedia", os.path.abspath("./DBTuning/OLTPBenchmark/config/memsql_wikipedia_config.xml"))

if __name__ == "__main__":
    run() 