# Counting the number of occurrences of consecutive patterns of inequalities
# of length 3 in inversion sequences
# Uses the file count_consec_ineq3.py and gen_inv_seq.py

import count_consec_ineq3
import gen_inv_seq

# Counts the occurrences of a consecutive pattern of inequalities of length 3
# among inversion sequences of a given length.
# Parameters: length is an integer; symbol 1 and symbol2 are strings from the
# list '<=', '>=', '<', '>', '=' and '!='.
# Returns a list [a0,a1,...,an] (say we are counting inversion
# sequences of lenght n), where ai is the number of sequences with
# exactly ai occurrences of the pattern.


def occur_ineq3(length, symbol1, symbol2):
    occur = [0] * length
    for sequence in gen_inv_seq.inv_seq(length):
        index = count_consec_ineq3.count_ineq3(sequence, symbol1, symbol2)
        occur[index] += 1
    return occur

# Obtains the inversion sequences of a given length with each number of
# occurrences of a given consecutive pattern of inequalities of length 3.
# Parameters: length is an integer; symbol 1 and symbol2 are strings from the
# list '<=', '>=', '<', '>', '=' and '!='.
# Returns a list of lists [a0,a1,...,an] (say we are counting inversion
# sequences of lenght n). Here ai is the list of sequences with exactly
# i occurrences, or 'None' if there are no sequences with i occurrences


def occur_list_ineq3(length, symbol1, symbol2):
    occur_list = ['None'] * length
    for sequence in gen_inv_seq.inv_seq(length):
        index = count_consec_ineq3.count_ineq3(sequence, symbol1, symbol2)
        if occur_list[index] == 'None':
            occur_list[index] = [sequence]
        else:
            occur_list[index].append(sequence)
    return occur_list
