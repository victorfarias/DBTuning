from DBTuning.OLTPBenchmark.install import install as install_OLTP
from DBTuning.MemSQL.install import install as install_mem


if __name__ == "__main__":
    install_mem()
    # install_OLTP()