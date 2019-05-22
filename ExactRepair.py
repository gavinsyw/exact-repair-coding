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
        self.inequalities = []
        self.equalities = []
        self.termNum = len(self.terms)

    def HGreaterThan0(self): # Shannon Inequality for H>0
        inequalities = []
        standardVec = [0 for i in range(self.termNum+1)]
        for i in range(self.termNum):
            standardVec[i] = -1
            inequalities.append(standardVec.copy())
            standardVec[i] = 0
        return inequalities

    def IGreaterThan0(self): # Shannon Inequality for I>0
        inequalities = []
        standardVec = [0 for i in range(self.termNum)]
        
        return None

if __name__ == "__main__":
    e = ExactRepair(4)
    e.HGreaterThan0()