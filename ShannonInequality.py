import numpy as np
import math
import itertools


class Entropy:
    def __init__(self, master, slave):
        """
        :param term: entropy term, string
        :return None
        """
        self.master = master
        self.slave = slave
    
    def __eq__(self, anoEntropy):
        return (self.master == anoEntropy.master and self.slave == anoEntropy.slave)
    
    def __str__(self):
        return str(self.master)+str(self.slave)
    

class JointEntropy:
    def __init__(self, terms, node_number):
        """
        :param terms: entropy terms, list
        :return None
        """
        self.entropies = [Entropy(term[0], term[1]) for term in terms]
        self.node_number = node_number
    
    def expand(self):
        """
        Expand the entropy terms as the paper introduced.
        :return None
        """
        change_flag = True
        while change_flag:
            change_flag = False
            for entropy_term in self.entropies:
                if entropy_term.master == entropy_term.slave:
                    i = entropy_term.master
                    for j in range(1, 1+self.node_number):
                        if i == j:
                            continue
                        else:
                            change_flag = self.add(Entropy(i, j))
            
            for j in range(1, 1+self.node_number):
                exist_flag = True
                for i in range(1, 1+self.node_number):
                    if i == j:
                        continue
                    else:
                        if Entropy(i, j) not in self.entropies:
                            exist_flag = False
                if exist_flag:
                    change_flag = self.add(Entropy(j, j))
                       
    def show(self):
        """
        show the entropy terms. Reconstruct the print if possible
        """
        print("Entropy Terms: ", [(item.master, item.slave) for item in self.entropies])
        print("Node Number: ", str(self.node_number))

    def items(self):
        return [str(entropy) for entropy in self.entropies]

    def __eq__(self, anoTerm):
        if len(self.entropies) != len(anoTerm.entropies):
            return False
        for entropy in self.entropies:
            if entropy not in anoTerm.entropies:
                return False
        return True
    
    def symmetricTerms(self, all_permutations):
        symmetricTerms = []
        for permutation in all_permutations:
            new_entropy_list = list()
            for entropy in self.entropies:
                if entropy.master == entropy.slave:
                    new_entropy_list.append([permutation[entropy.master-1], permutation[entropy.master-1]])
                else:
                    new_entropy_list.append([permutation[entropy.master-1], permutation[entropy.slave-1]])
            newJointEntropy = JointEntropy(new_entropy_list, 4)
            if newJointEntropy != self and newJointEntropy not in symmetricTerms:
                symmetricTerms.append(newJointEntropy)
        return symmetricTerms
    
    def add(self, anoEntropy):
        if anoEntropy not in self.entropies:
            (self.entropies).append(anoEntropy)
            return True
        else:
            return False
            

class ShannonInequality:
    def __init__(self, JointEntropies, number):
        """
        :param terms: joint entropy terms, list with positive or negative
        :param number: the number the joint terms are smaller to
        :return None
        """
        self.jointTerms = JointEntropies
        self.number = number
    

class ShannonInequalities:
    def __init__(self, inequalities):
        """
        :param inequalities: list of shannon inequality
        :return None
        """
        self.inequalities = inequalities
    
    def generateMatrix(self):
        """
        :param None
        :return the inequality coefficient matrix, the number vector
        """

if __name__ == "__main__":
    e = Entropy(1, 1)
    es = JointEntropy([[1, 1], [2, 2]], 4)
    es.show()
    es.expand()
    es.show()
    print("Symmetric Terms:")
    all_permutations = list(itertools.permutations([i for i in range(1, 5)], 4))
    for i in es.symmetricTerms(all_permutations):
        i.show()
