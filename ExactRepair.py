import ShannonInequality as SI
from Reduction import Reduction
import numpy as np
import scipy.optimize as op
import matplotlib.pyplot
import itertools
import math

class ExactRepair:
    def __init__(self, nodeNum):
        self.nodeNum = nodeNum
        reduction = Reduction(nodeNum)
        print("Initializing ...")
        self.terms = reduction.termTable()
        print("Reduction Complete, item number: ", len(self.terms))


if __name__ == "__main__":
    e = ExactRepair(4)
