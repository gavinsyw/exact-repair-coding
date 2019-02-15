import ShannonInequality as si
import numpy as np
import scipy.optimize as op
import matplotlib.pyplot
import itertools

class ExactRepair:
    def __init__(self, nodeNum):
        self.nodeNum = nodeNum
    
    def termTable(self):
        """ 
        :return Table of terms
        """
        all_terms = ["W"+str(i) for i in range(1, 1+self.nodeNum)] + \
                ["S"+str(i)+str(j) for i in range(1, 1+self.nodeNum) \
                for j in range(1, 1+self.nodeNum) if i != j]
        termNum = len(all_terms)
        d = dict()
        existingTerms = list()
        all_iter = list()
        for i in range(1, 1+termNum):
            all_iter += list(itertools.combinations(all_terms, i))
        time_count = 0
        for item in all_iter:
            e = si.JointEntropy(item, self.nodeNum)
            e.expand()
            e_items = e.items()
            e_items.sort()
            e_items = tuple(e_items)
            if tuple(e_items) not in existingTerms:
                existingTerms.append(e_items)
            time_count += 1
            if time_count % 1024 == 0:
                print("Completed:", int(time_count / 65536 * 100), "%")
        return existingTerms

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
    a = ExactRepair(4)
    terms = a.termTable()
    print(len(terms))
