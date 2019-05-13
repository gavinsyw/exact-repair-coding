import ShannonInequality as si
import numpy as np
import scipy.optimize as op
import matplotlib.pyplot
import itertools
import math

class ExactRepair:
    def __init__(self, nodeNum):
        self.nodeNum = nodeNum
        self.all_terms = ["W"+str(i) for i in range(1, 1+self.nodeNum)] + \
                ["S"+str(i)+str(j) for i in range(1, 1+self.nodeNum) \
                for j in range(1, 1+self.nodeNum) if i != j]
    
    def build_symmetricity(self):
        all_terms = self.all_terms
        all_iter = list()
        termNum = len(all_terms)
        for i in range(1, 1+termNum):
            all_iter += list(itertools.combinations(all_terms, i))
        reduced_terms = []
        all_permutations = list(itertools.permutations([str(i) for i in range(1, 1+self.nodeNum)], self.nodeNum))
        for i in all_iter:
            entropy = si.JointEntropy(i, self.nodeNum)
            symmetric_entropies = entropy.symmetricTerms(all_permutations)
            for symmetric_entropy in symmetric_entropies:
                try:
                    all_iter.remove(symmetric_entropy)
                except ValueError:
                    continue
            reduced_terms.append(i)
            print(i)
        return reduced_terms

    def termTable(self, iter_terms = []):
        """ 
        :return Table of terms
        """
        all_terms = self.all_terms
        termNum = len(all_terms)
        d = dict()
        existingTerms = list()
        all_iter = iter_terms
        if all_iter == []:
            for i in range(1, 1+termNum):
                all_iter += list(itertools.combinations(all_terms, i))
        time_count = 0
        total_number = math.pow(2, self.nodeNum * self.nodeNum)
        percent_number = int(total_number / 100)
        for item in all_iter:
            e = si.JointEntropy(item, self.nodeNum)
            e.expand()
            e_items = e.items()
            e_items.sort()
            e_items = tuple(e_items)
            if tuple(e_items) not in existingTerms:
                existingTerms.append(e_items)
            time_count += 1
            if time_count % percent_number == 0:
                print("Completed:", int(time_count / total_number * 100), "%")
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


def build_symmetricity(all_iter, nodeNum):
    """
    :para L: list of entropy items in strings
    :return the symmetry reduction of l
    """
    all_terms = ["W"+str(i) for i in range(1, 1+nodeNum)] + \
                ["S"+str(i)+str(j) for i in range(1, 1+nodeNum) \
                for j in range(1, 1+nodeNum) if i != j]
    termNum = len(all_terms)
    reduced_terms = []
    all_permutations = list(itertools.permutations([str(i) for i in range(1, 1+nodeNum)], nodeNum))
    for i in all_iter:
        entropy = si.JointEntropy(i, nodeNum)
        symmetric_entropies = entropy.symmetricTerms(all_permutations)
        for symmetric_entropy in symmetric_entropies:
            try:
                all_iter.remove(symmetric_entropy)
            except ValueError:
                continue
        reduced_terms.append(i)
    return reduced_terms


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
    a = ExactRepair(5)
    terms = a.termTable()
    print(len(terms))
    print(len(build_symmetricity(terms, 4)))
