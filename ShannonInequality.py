import numpy as np
import math
import itertools


class Entropy:
    def __init__(self, term, total_number):
        """
        :param term: entropy term, string
        :return None
        """
        self.term = term
        self.total_number = total_number
        self.property = term[0]
        self.master = term[1]
        if self.property == 'S':
            self.slave = term[2]
        else:
            self.slave = ''
    

class JointEntropy:
    def __init__(self, terms, total_number):
        """
        :param terms: entropy terms, list
        :return None
        """
        self.entropies = [Entropy(term, total_number) for term in terms]
        self.total_number = total_number
    
    def expand(self):
        """
        Expand the entropy terms as the paper introduced.
        :return None
        """
        W_list = [Entropy('W'+str(i), self.total_number) for i in range(1, 1+self.total_number)]
        S_list = [Entropy('S'+str(i)+str(j), self.total_number) \
             for i in range(1, 1+self.total_number) for j in range(self.total_number) if i != j]
        change_flag = True
        while change_flag:
            change_flag = False
            for entropy_term in self.entropies:
                if entropy_term.property == 'W':
                    for generate_term in [Entropy('S'+str(entropy_term.master)+j, self.total_number)  \ 
                        for j in range(1, 1+self.total_number) if j != entropy_term.master]
    
    def show(self):
        """
        show the entropy terms. Reconstruct the print if possible
        """
        print("Entropy Terms: ", [str(item.term) for item in self.entropies])
        print("Total Number: ", str(self.total_number))
    

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
    print("test")
