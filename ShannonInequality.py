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
        self.master = int(term[1])
        if self.property == 'S':
            self.slave = int(term[2])
        else:
            self.slave = 0
    
    def __eq__(self, anoEntropy):
        if self.term == anoEntropy.term and self.total_number == anoEntropy.total_number:
            return True
        else:
            return False
    

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
        change_flag = True
        while change_flag:
            # self.show()
            change_flag = False
            for entropy_term in self.entropies:
                if entropy_term.property == 'W':
                    i = entropy_term.master
                    for j in range(1, 1+self.total_number):
                        if i == j:
                            continue
                        else:
                            if Entropy('S'+str(i)+str(j), self.total_number) not in self.entropies:
                                change_flag = True
                                (self.entropies).append(Entropy('S'+str(i)+str(j), self.total_number))
                                # print("added: S"+str(i)+str(j))
            
            for j in range(1, 1+self.total_number):
                exist_flag = True
                for i in range(1, 1+self.total_number):
                    if i == j:
                        continue
                    else:
                        if Entropy('S'+str(i)+str(j), self.total_number) not in self.entropies:
                            exist_flag = False
                if exist_flag:
                    if Entropy('W'+str(j), self.total_number) not in self.entropies:
                        change_flag = True
                        (self.entropies).append(Entropy('W'+str(j), self.total_number))
                        # print("added: W"+str(j))
    
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
    e = Entropy("W1", 4)
    es = JointEntropy(["W1", "W2", "W3"], 4)
    es.show()
    es.expand()
    es.show()