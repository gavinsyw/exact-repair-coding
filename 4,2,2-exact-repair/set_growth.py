from bidict import bidict
import itertools


# coding method: W1, W2, W3, W4, S12, S13, S14, S21, S23, S24, S31, S32, S34, S41, S42, S43, a 16-bit number
#          bits:  0,  1,  2,  3,   4,   5,   6,   7,   8,   9,  10,  11,  12,  13,  14,  15

all_sets = [('0000000000000000'+bin(x)[2:])[-16:] for x in range(0x0001, 0xFFFF+1)]

all_permutation = list(itertools.permutations(['1', '2', '3', '4'], 4))


bit_position = {"W1": 0,
                "W2": 1,
                "W3": 2,
                "W4": 3,
                "S12": 4,
                "S13": 5,
                "S14": 6,
                "S21": 7,
                "S23": 8,
                "S24": 9,
                "S31": 10,
                "S32": 11,
                "S34": 12,
                "S41": 13,
                "S42": 14,
                "S43": 15}

bit_position = bidict(bit_position)

final_set = []


def symmetric_set(s):
    """
    :param s: string 0x0001-0xFFFF
    :return: all symmetry of s
    """
    symmetry = []
    entropy_terms = [bit_position.inv[a] for a in range(0, 16) if s[a] == '1']
    for i in all_permutation:
        symmetric_str = ['0' for a in range(0, 16)]
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
    """
    :param s: string, 0x0001-0xFFFF
    :return: none
    put the growth of s into result_set
    """
    growth = s
    flag = False
    for i in range(0, 4):
        if growth[i] == '1':
            if growth[3*i+4] != '1' or growth[3*i+5] != '1' or growth[3*i+6] != '1':
                growth[3 * i + 4] = growth[3 * i + 5] = growth[3 * i + 6] = '1'
                flag = True
    if growth[7] == '1' and growth[10] == '1' and growth[13] == '1':
        if growth[0] != '1':
            growth[0] = '1'
            flag = True
    if growth[4] == '1' and growth[11] == '1' and growth[14] == '1':
        if growth[1] != '1':
            growth[1] = '1'
            flag = True
    if growth[5] == '1' and growth[8] == '1' and growth[15] == '1':
        if growth[2] != '1':
            growth[2] = '1'
            flag = True
    if growth[6] == '1' and growth[9] == '1' and growth[12] == '1':
        if growth[3] != '1':
            growth[3] = '1'
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
        for symmetry_item in all_symmetry_items:
            if symmetry_item in s:
                s.remove(symmetry_item)


print("growth set: ")
all_growth(all_sets, final_set)
print(len(final_set))
symmetry_reduction(final_set)
final_set.sort()
for x in final_set:
    print(x)
print(len(final_set))
