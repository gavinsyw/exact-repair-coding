import ShannonInequality
import numpy as np
import scipy.optimize as op
import matplotlib.pyplot

class ExactRepair:
    def __init__(self, nodeNum):
        self.nodeNum = nodeNum
    
    def generateInequalities(self):
        """
        :return inequalities
        """
        return np.array([[]])
    
    def searchBound(self):
        """
        :return boundImg
        """
        return np.array([[]])
    
    def computeProof(self):
        """
        :return usedInequalities
        """
        return []

if __name__ == "__main__":
    print("Test")