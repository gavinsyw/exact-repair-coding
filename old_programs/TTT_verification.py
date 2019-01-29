from er_optimization_III_II_II import *
from er_set_growth_III_II_II import *
from scipy import optimize as op
import numpy as np
import sys


if __name__ == '__main__':
    final_set = []
    inequality_matrix = []
    inequality_vector = []
    er_set_growth_III_II_II.all_growth(all_sets, final_set)
    er_set_growth_III_II_II.symmetry_reduction(final_set)
    final_set.append('000000000')
    final_set.sort()
    print final_set
    generate_shannon_inequalities_H(final_set, inequality_matrix, inequality_vector)
    generate_shannon_inequalities_I(final_set, inequality_matrix, inequality_vector)
    inequality_matrix, inequality_vector = np.array(inequality_matrix), np.array(inequality_vector)
    # print inequality_matrix
    # print inequality_vector

    lamLength = len(inequality_matrix)

    At = np.transpose(inequality_matrix)
    c = [0 for i in range(len(At))]
    c[-1] = -1
    c[7] = 0
    c[1] = 1
    c = np.array(c)

    print At, c

    result = op.linprog(np.array([-1 for i in range(lamLength)]), A_ub=At, b_ub=c)
    print result
