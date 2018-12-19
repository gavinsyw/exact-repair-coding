from bidict import bidict
import itertools


# coding method: W1, W2, W3, S12, S13, S21, S23, S31, S32, a 9-bit number
#          bits:  0,  1,  2,   3,   4,   5,   6,   7,   8

all_sets = [('000000000'+bin(x)[2:])[-9:] for x in range(0x1, 0x1FF+1)]

all_permutation = list(itertools.permutations(['1', '2', '3'], 3))

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

final_set = []


def symmetric_set(s):
    symmetry = []
    entropy_terms = [bit_position.inv[a] for a in range(0, 9) if s[a] == '1']
    for i in all_permutation:
        symmetric_str = ['0' for a in range(0, 9)]
        for term in entropy_terms:
            newterm = list(term)
            if term[0] == 'W':
                newterm[1] = i[int(term[1])-1]
            elif term[0] == 'S':
                newterm[1] = i[int(term[1])-1]
                newterm[2] = i[int(term[2])-1]
            symmetric_str[bit_position[''.join(newterm)]] = '1'
        symmetric_str = ''.join(symmetric_str)
        if symmetric_str != s:
            symmetry.append(symmetric_str)
    return symmetry


def set_growth(s, result_set):
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
        result = ''.join(growth)
        if result not in result_set:
            result_set.append(result)
            return
    else:
        set_growth(growth, result_set)
        return


def all_growth(set1, set2):
    """
    :param set1: original set
    :param set2: final set
    :return: none
    """
    for i in set1:
        # print i
        set_growth(list(i), set2)


def symmetry_reduction(s):
    """
    do symmetry reduction based on the previous 9 relationships
    """
    for i in s:
        all_symmetry_items = symmetric_set(i)
        if i == '000001010':
            print i, all_symmetry_items
        for symmetry_item in all_symmetry_items:
            if symmetry_item in s:
                s.remove(symmetry_item)


# print "growth set: "
# all_growth(all_sets, final_set)
# symmetry_reduction(final_set)
# final_set.sort()
# print len(final_set)
