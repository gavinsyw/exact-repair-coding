from bidict import bidict
import sys
import scipy.optimize as op
import numpy as np
import itertools
import set_growth

# coding method: W1, W2, W3, S12, S13, S21, S23, S31, S32, a 9-bit number
#          bits:  0,  1,  2,   3,   4,   5,   6,   7,   8
# B = 1, in hypothesis

H_A = 1

all_sets = [('000000000'+bin(x)[2:])[-9:] for x in range(0x1, 0x1FF+1)]

bit_position = {"W1": 0,
                "W2": 1,
                "W3": 2,
                "S12": 3,
                "S13": 4,
                "S21": 5,
                "S23": 6,
                "S31": 7,
                "S32": 8}

bit_position = bidict(bit_position)

all_permutation = list(itertools.permutations(['1', '2', '3'], 3))


def find_growth(s):
    growth = s
    flag = False
    for i in range(0, 3):
        if growth[i] == '1':
            if growth[2*i+3] != '1' or growth[2*i+4] != '1':
                growth[2*i+3] = growth[2*i+4] = '1'
                flag = True
    if growth[5] == '1' and growth[7] == '1':
        if growth[0] != '1':
            growth[0] = '1'
            flag = True
    if growth[3] == '1' and growth[8] == '1':
        if growth[1] != '1':
            growth[1] = '1'
            flag = True
    if growth[4] == '1' and growth[6] == '1':
        if growth[2] != '1':
            growth[2] = '1'
            flag = True
    if not flag:
        # save the result
        return ''.join(growth)
    else:
        return find_growth(growth)


def union(s1, s2):
    """
    :param s1: bin str
    :param s2: bin str
    :return: s1 or s2
    """
    s = list(s1)
    for i in range(len(s2)):
        if s2[i] == '1':
            s[i] = '1'
    return "".join(s)


def intersect(s1, s2):
    """
    :param s1: bin str
    :param s2: bin str
    :return: s1 and s2
    """
    s = list(s1)
    for i in range(len(s2)):
        if s2[i] == '0':
            s[i] = '0'
    return "".join(s)


def findInSet(element_set, s):
    """
    :param element_set: list, element_set
    :param s: bin str
    :return: the order of s or symmetry of s in element_set
    """
    s_semmetry = find_growth(list(s))
    entropy_terms = [bit_position.inv[a] for a in range(0, 9) if s_semmetry[a] == '1']
    symmetry_item = 0
    while s_semmetry not in element_set:
        s_semmetry = ['0' for a in range(9)]
        i = all_permutation[symmetry_item]
        for term in entropy_terms:
            newterm = list(term)
            if term[0] == 'W':
                newterm[1] = i[int(term[1])-1]
            elif term[0] == 'S':
                newterm[1] = i[int(term[1])-1]
                newterm[2] = i[int(term[2])-1]
            s_semmetry[bit_position[''.join(newterm)]] = '1'
        s_semmetry = ''.join(s_semmetry)
        symmetry_item += 1
    return element_set.index("".join(s_semmetry))


def generate_shannon_inequalities_H(element_set, iem_left, iem_right):
    general_vec = [0 for i in range(len(element_set))]
    general_vec[10] = -1
    for i in range(len(element_set)-1):
        general_vec[i] = 1
        iem_left.append(tuple(general_vec))
        iem_right.append(0)
        general_vec[i] = 0
    return


def generate_shannon_inequalities_I(element_set, iem_left, iem_right):
    general_vec = [0 for i in range(len(element_set))]
    for i in range(9):
        for j in range(i):
            element_1 = ['0' for i in range(9)]
            element_1[i] = '1'
            element_1 = ''.join(element_1)

            element_2 = ['0' for i in range(9)]
            element_2[j] = '1'
            element_2 = ''.join(element_2)

            element_3 = union(element_1, element_2)
            element_4 = intersect(element_1, element_2)
            k = findInSet(element_set, element_3)
            l = findInSet(element_set, element_4)
            element_1 = findInSet(element_set, ''.join(element_1))
            tmp1 = element_1
            element_1 = element_set[element_1]
            element_2 = findInSet(element_set, ''.join(element_2))
            if element_1 == element_2:
                continue
            tmp2 = element_2
            element_2 = element_set[element_2]
            general_vec[tmp1] = general_vec[tmp2] = -1
            general_vec[k] += 1
            general_vec[l] += 1
            if tuple(general_vec) not in iem_left:
                iem_left.append(tuple(general_vec))
                iem_right.append(0)
            general_vec[i] = general_vec[j] = general_vec[k] = general_vec[l] = 0

            # print tmp1, element_1, tmp2, element_2, k, element_3, l, element_4
    return


if __name__ == '__main__':
    final_set = []
    inequality_matrix = []
    inequality_vector = []
    set_growth.all_growth(all_sets, final_set)
    set_growth.symmetry_reduction(final_set)
    final_set.append('000000000')
    final_set.sort()
    print(final_set)
    generate_shannon_inequalities_H(final_set, inequality_matrix, inequality_vector)
    generate_shannon_inequalities_I(final_set, inequality_matrix, inequality_vector)
    inequality_matrix.append(tuple([0 for i in range(7)]+[1]+[0 for i in range(8, len(final_set))]))
    inequality_vector.append(1)
    # inequality_matrix.append(tuple([0 for i in range(7)] + [-1] + [0 for i in range(8, len(final_set))]))
    # inequality_vector.append(0)
    equality_matrix = list()
    equality_matrix.append(np.array([1]+[0 for i in range(len(final_set)-1)]))
    equality_matrix.append(np.array([0 for i in range(len(final_set)-1)]+[1]))
    equality_vector = [0, 1]
    c = [0 for i in range(len(final_set))]
    c[1] = 1
    print(np.array(inequality_matrix), inequality_vector)
    result = op.linprog(np.array(c), A_ub=np.array(inequality_matrix), b_ub=np.array(inequality_vector),
                        A_eq=np.array(equality_matrix), b_eq=np.array(equality_vector))
    print(result)
