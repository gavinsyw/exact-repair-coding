import ShannonInequality as SI
import numpy as np
import scipy.optimize as op
import matplotlib.pyplot
import itertools
import math

class ExactRepair:
    def __init__(self, nodeNum):
        self.nodeNum = nodeNum
        self.all_terms = [[i, j] for i in range(1, 1+nodeNum) for j in range(1, 1+nodeNum)]
    
    def build_symmetric(self, all_iter):
        """
        :para L: list of entropy items in strings
        :return the symmetry reduction of l
        """
        nodeNum = self.nodeNum
        all_terms = self.all_terms
        termNum = len(all_terms)
        reduced_terms = []
        all_permutations = list(itertools.permutations([i for i in range(1, 1+nodeNum)], nodeNum))
        for i in all_iter:
            i = [[int(j[0]), int(j[1])] for j in i]
            entropy = SI.JointEntropy(i, nodeNum)
            symmetric_entropies = entropy.symmetricTerms(all_permutations)
            for symmetric_entropy in symmetric_entropies:
                symmetric_entropy = tuple(symmetric_entropy.items())
                if symmetric_entropy in all_iter:
                    all_iter.remove(symmetric_entropy)
            reduced_terms.append(SI.JointEntropy(i, 4))
        return reduced_terms


    def termTable(self, iter_terms = []):
        """ 
        :return Table of terms
        """
        all_terms = self.all_terms
        termNum = len(all_terms)
        existingTerms = list()
        all_iter = iter_terms
        if all_iter == []:
            for i in range(1, 1+termNum):
                all_iter += list(itertools.combinations(all_terms, i))
        time_count = 0
        total_number = math.pow(2, self.nodeNum * self.nodeNum)
        percent_number = int(total_number / 100)
        for item in all_iter:
            e = SI.JointEntropy(item, self.nodeNum)
            e.expand()
            e_items = e.items()
            e_items.sort()
            e_items = tuple(e_items)
            if tuple(e_items) not in existingTerms:
                existingTerms.append(e_items)
            time_count += 1
            if time_count % percent_number == 0:
                print("Completed:", int(time_count / total_number * 100), "%")
        existingTerms = self.build_symmetric(existingTerms)
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


def write_to_file(l, files):
    """
    :para l: list of entropy terms, in entropy terms or in strings
    :return None
    """
    with open(files, "w") as f:
        for i in l:
            f.write(i)
            f.write("\n")
    f.close()
    return


if __name__ == "__main__":
    print("Test")
    a = ExactRepair(4)
    terms = a.termTable()
    print(len(terms))
