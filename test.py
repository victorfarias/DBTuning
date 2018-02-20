import numpy as np

from DBTuning.core.optimizer import Optimizer
from DBTuning.DummyDB.api import DummyDB

if __name__ == "__main__":
    np.random.seed(1)
    opt = Optimizer(DummyDB())
    opt.run_optimization()
