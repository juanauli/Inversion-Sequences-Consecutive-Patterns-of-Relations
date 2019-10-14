# Finding and counting inversion sequences avoiding
# consecutive patterns of inequalities of length 3
# Uses the file consec_detect_ineq3.py and gen_inv_seq.py


import consec_detect_ineq3
import gen_inv_seq


# Counts the number of sequences in a collection that avoid
# a given pattern of inequalities of length 3.
# Parameters: collection is a list of lists, symbol1 and symbol2 are strings.
# Returns the number of sequences avoiding the pattern, an integer.


def count_avoiding_ineq3(collection, symbol1, symbol2):
    counter = 0
    for sequence in collection:
        if not consec_detect_ineq3.detect_ineq3(sequence, symbol1, symbol2):
            counter += 1
    return counter

# Finds the sequences in a collection that avoid a given pattern of
# inequalities of length 3.
# Parameters: collection is a list of lists, symbol1 and symbol2 are strings.
# Returns the sequences avoiding the pattern, a list.


def find_avoiding_ineq3(collection, symbol1, symbol2):
    avoiding_seq = list()
    for sequence in collection:
        if not consec_detect_ineq3.detect_ineq3(sequence, symbol1, symbol2):
            avoiding_seq.append(sequence)
    return avoiding_seq

# Counts the number of inversion sequences of a given length
# that avoid a given pattern of inequalities of length 3.
# Parameters: length is an integer, symbol1 and symbol2 are strings.
# Returns the number of inversion sequences of the given length
# that avoid the pattern, an integer.


def count_inv_avoiding_ineq3(length, symbol1, symbol2):
    return count_avoiding_ineq3(gen_inv_seq.inv_seq(length), symbol1, symbol2)

# Finds the inversion sequences of a given length that avoid
# a given pattern of inequalities of length 3.
# Parameters: length is an integer, symbol1 and symbol2 are strings.
# Returns the inversion sequences of the given length
# that avoid the pattern of inequalities, a list.


def find_inv_avoiding_ineq3(length, symbol1, symbol2):
    return find_avoiding_ineq3(gen_inv_seq.inv_seq(length), symbol1, symbol2)
