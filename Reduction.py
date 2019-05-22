import ShannonInequality as SI
import numpy as np
import scipy.optimize as op
import matplotlib.pyplot
import itertools
import math

class Reduction:
    def __init__(self, nodeNum):
        self.nodeNum = nodeNum
        self.all_terms = [[i, j] for i in range(1, 1+nodeNum) for j in range(1, 1+nodeNum)]
    
    def build_symmetric(self, termtable):
        """
        :para L: list of entropy items in strings
        :return the symmetry reduction of l
        """
        nodeNum = self.nodeNum
        termNum = nodeNum * nodeNum
        reduced_terms = []
        all_permutations = list(itertools.permutations([i for i in range(1, 1+nodeNum)], nodeNum))
        for jointTerm in termtable:
            symmetric_entropies = jointTerm.symmetricTerms(all_permutations)
            for symmetric_entropy in symmetric_entropies:
                if symmetric_entropy in termtable:
                    termtable.remove(symmetric_entropy)
            reduced_terms.append(jointTerm)
        return reduced_terms


    def termTable(self):
        """ 
        :return Table of terms
        """
        all_terms = self.all_terms
        termNum = len(all_terms)
        existingTerms = list()
        all_iter = []
        for i in range(1, 1+termNum):
            all_iter += list(itertools.combinations(all_terms, i))
        time_count = 0
        total_number = math.pow(2, self.nodeNum * self.nodeNum)
        percent_number = int(total_number / 10)
        for item in all_iter:
            e = SI.JointEntropy(item, self.nodeNum)
            e.expand()
            if e not in existingTerms:
                existingTerms.append(e)
            time_count += 1
            if time_count % percent_number == 0:
                print("Completed:", int(time_count / total_number * 93), "%")
        existingTerms = self.build_symmetric(existingTerms)
        return existingTerms


if __name__ == "__main__":
    print("Test")
    a = Reduction(4)
    terms = a.termTable()
    print(len(terms))
