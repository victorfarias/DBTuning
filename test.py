from DBTuning.core.optimizer import Optimizer
from DBTuning.DummyDB.api import DummyDB

if __name__ == "__main__":
    opt = Optimizer(DummyDB())
    