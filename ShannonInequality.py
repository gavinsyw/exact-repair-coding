import numpy as np
import math
import itertools

class Entropy:
    def __init__(self, term):
        """
        :param term: entropy term, string
        :return None
        """
        self.term = term
    

class JointEntropy:
    def __init__(self, terms):
        """
        :param terms: entropy terms, list
        :return None
        """
        self.terms = terms
        self.entropies = [Entropy(term) for term in terms]
    
    def expand(self):
        """
        Expand the entropy terms as the paper introduced.
        Return the flag if the entropy terms has changed.
        :return flag (modified: true, else: false)
        """
    
    def show(self):
        """
        show the entropy terms. Reconstruct the print if possible
        """
    

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
