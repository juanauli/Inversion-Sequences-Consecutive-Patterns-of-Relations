# Count occurrences of consecutive patterns of inequalities of length 3

# Counts occurrences of the pattern "<=, <=".


def count_leq_leq(sequence):
    index = 0
    counter = 0
    while index < len(sequence) - 2:
        if sequence[index] <= sequence[index + 1] <= sequence[index + 2]:
            counter += 1
        index += 1
    return counter

# Counts occurrences of the pattern "<=, >=".


def count_leq_geq(sequence):
    index = 0
    counter = 0
    while index < len(sequence) - 2:
        if sequence[index] <= sequence[index + 1] >= sequence[index + 2]:
            counter += 1
        index += 1
    return counter

# Counts occurrences of the pattern "<=, <".


def count_leq_less(sequence):
    index = 0
    counter = 0
    while index < len(sequence) - 2:
        if sequence[index] <= sequence[index + 1] < sequence[index + 2]:
            counter += 1
        index += 1
    return counter

# Counts occurrences of the pattern "<=, >".


def count_leq_great(sequence):
    index = 0
    counter = 0
    while index < len(sequence) - 2:
        if sequence[index] <= sequence[index + 1] > sequence[index + 2]:
            counter += 1
        index += 1
    return counter

# Counts occurrences of the pattern "<=, =".


def count_leq_eq(sequence):
    index = 0
    counter = 0
    while index < len(sequence) - 2:
        if sequence[index] <= sequence[index + 1] == sequence[index + 2]:
            counter += 1
        index += 1
    return counter

# Counts occurrences of the pattern "<=, !=".


def count_leq_neq(sequence):
    index = 0
    counter = 0
    while index < len(sequence) - 2:
        if sequence[index] <= sequence[index + 1] != sequence[index + 2]:
            counter += 1
        index += 1
    return counter

# Counts occurrences of the pattern ">=, <=".


def count_geq_leq(sequence):
    index = 0
    counter = 0
    while index < len(sequence) - 2:
        if sequence[index] >= sequence[index + 1] <= sequence[index + 2]:
            counter += 1
        index += 1
    return counter

# Counts occurrences of the pattern ">=, >=".


def count_geq_geq(sequence):
    index = 0
    counter = 0
    while index < len(sequence) - 2:
        if sequence[index] >= sequence[index + 1] >= sequence[index + 2]:
            counter += 1
        index += 1
    return counter

# Counts occurrences of the pattern ">=, <".


def count_geq_less(sequence):
    index = 0
    counter = 0
    while index < len(sequence) - 2:
        if sequence[index] >= sequence[index + 1] < sequence[index + 2]:
            counter += 1
        index += 1
    return counter

# Counts occurrences of the pattern ">=, >".


def count_geq_great(sequence):
    index = 0
    counter = 0
    while index < len(sequence) - 2:
        if sequence[index] >= sequence[index + 1] > sequence[index + 2]:
            counter += 1
        index += 1
    return counter

# Counts occurrences of the pattern ">=, =".


def count_geq_eq(sequence):
    index = 0
    counter = 0
    while index < len(sequence) - 2:
        if sequence[index] >= sequence[index + 1] == sequence[index + 2]:
            counter += 1
        index += 1
    return counter

# Counts occurrences of the pattern ">=, !=".


def count_geq_neq(sequence):
    index = 0
    counter = 0
    while index < len(sequence) - 2:
        if sequence[index] >= sequence[index + 1] != sequence[index + 2]:
            counter += 1
        index += 1
    return counter

# Counts occurrences of the pattern "<, <=".


def count_less_leq(sequence):
    index = 0
    counter = 0
    while index < len(sequence) - 2:
        if sequence[index] < sequence[index + 1] <= sequence[index + 2]:
            counter += 1
        index += 1
    return counter


# Counts occurrences of the pattern "<, >=".


def count_less_geq(sequence):
    index = 0
    counter = 0
    while index < len(sequence) - 2:
        if sequence[index] < sequence[index + 1] >= sequence[index + 2]:
            counter += 1
        index += 1
    return counter

# Counts occurrences of the pattern "<, <".


def count_less_less(sequence):
    index = 0
    counter = 0
    while index < len(sequence) - 2:
        if sequence[index] < sequence[index + 1] < sequence[index + 2]:
            counter += 1
        index += 1
    return counter

# Counts occurrences of the pattern "<, >".


def count_less_great(sequence):
    index = 0
    counter = 0
    while index < len(sequence) - 2:
        if sequence[index] < sequence[index + 1] > sequence[index + 2]:
            counter += 1
        index += 1
    return counter

# Counts occurrences of the pattern "<, =".


def count_less_eq(sequence):
    index = 0
    counter = 0
    while index < len(sequence) - 2:
        if sequence[index] < sequence[index + 1] == sequence[index + 2]:
            counter += 1
        index += 1
    return counter

# Counts occurrences of the pattern "<, !=".


def count_less_neq(sequence):
    index = 0
    counter = 0
    while index < len(sequence) - 2:
        if sequence[index] < sequence[index + 1] != sequence[index + 2]:
            counter += 1
        index += 1
    return counter

# Counts occurrences of the pattern ">, <=".


def count_great_leq(sequence):
    index = 0
    counter = 0
    while index < len(sequence) - 2:
        if sequence[index] > sequence[index + 1] <= sequence[index + 2]:
            counter += 1
        index += 1
    return counter

# Counts occurrences of the pattern ">, >=".


def count_great_geq(sequence):
    index = 0
    counter = 0
    while index < len(sequence) - 2:
        if sequence[index] > sequence[index + 1] >= sequence[index + 2]:
            counter += 1
        index += 1
    return counter

# Counts occurrences of the pattern ">, <".


def count_great_less(sequence):
    index = 0
    counter = 0
    while index < len(sequence) - 2:
        if sequence[index] > sequence[index + 1] < sequence[index + 2]:
            counter += 1
        index += 1
    return counter

# Counts occurrences of the pattern ">, >".


def count_great_great(sequence):
    index = 0
    counter = 0
    while index < len(sequence) - 2:
        if sequence[index] > sequence[index + 1] > sequence[index + 2]:
            counter += 1
        index += 1
    return counter

# Counts occurrences of the pattern ">, =".


def count_great_eq(sequence):
    index = 0
    counter = 0
    while index < len(sequence) - 2:
        if sequence[index] > sequence[index + 1] == sequence[index + 2]:
            counter += 1
        index += 1
    return counter

# Counts occurrences of the pattern ">, !=".


def count_great_neq(sequence):
    index = 0
    counter = 0
    while index < len(sequence) - 2:
        if sequence[index] > sequence[index + 1] != sequence[index + 2]:
            counter += 1
        index += 1
    return counter

# Counts occurrences of the pattern "=, <=".


def count_eq_leq(sequence):
    index = 0
    counter = 0
    while index < len(sequence) - 2:
        if sequence[index] == sequence[index + 1] <= sequence[index + 2]:
            counter += 1
        index += 1
    return counter

# Counts occurrences of the pattern "=, >=".


def count_eq_geq(sequence):
    index = 0
    counter = 0
    while index < len(sequence) - 2:
        if sequence[index] == sequence[index + 1] >= sequence[index + 2]:
            counter += 1
        index += 1
    return counter

# Counts occurrences of the pattern "=, <".


def count_eq_less(sequence):
    index = 0
    counter = 0
    while index < len(sequence) - 2:
        if sequence[index] == sequence[index + 1] < sequence[index + 2]:
            counter += 1
        index += 1
    return counter

# Counts occurrences of the pattern "=, >".


def count_eq_great(sequence):
    index = 0
    counter = 0
    while index < len(sequence) - 2:
        if sequence[index] == sequence[index + 1] > sequence[index + 2]:
            counter += 1
        index += 1
    return counter

# Counts occurrences of the pattern "=, =".


def count_eq_eq(sequence):
    index = 0
    counter = 0
    while index < len(sequence) - 2:
        if sequence[index] == sequence[index + 1] == sequence[index + 2]:
            counter += 1
        index += 1
    return counter

# Counts occurrences of the pattern "=, !=".


def count_eq_neq(sequence):
    index = 0
    counter = 0
    while index < len(sequence) - 2:
        if sequence[index] == sequence[index + 1] != sequence[index + 2]:
            counter += 1
        index += 1
    return counter

# Counts occurrences of the pattern "!=, <=".


def count_neq_leq(sequence):
    index = 0
    counter = 0
    while index < len(sequence) - 2:
        if sequence[index] != sequence[index + 1] <= sequence[index + 2]:
            counter += 1
        index += 1
    return counter

# Counts occurrences of the pattern "!=, >=".


def count_neq_geq(sequence):
    index = 0
    counter = 0
    while index < len(sequence) - 2:
        if sequence[index] != sequence[index + 1] >= sequence[index + 2]:
            counter += 1
        index += 1
    return counter

# Counts occurrences of the pattern "!=, <".


def count_neq_less(sequence):
    index = 0
    counter = 0
    while index < len(sequence) - 2:
        if sequence[index] != sequence[index + 1] < sequence[index + 2]:
            counter += 1
        index += 1
    return counter

# Counts occurrences of the pattern "!=, >".


def count_neq_great(sequence):
    index = 0
    counter = 0
    while index < len(sequence) - 2:
        if sequence[index] != sequence[index + 1] > sequence[index + 2]:
            counter += 1
        index += 1
    return counter

# Counts occurrences of the pattern "!=, =".


def count_neq_eq(sequence):
    index = 0
    counter = 0
    while index < len(sequence) - 2:
        if sequence[index] != sequence[index + 1] == sequence[index + 2]:
            counter += 1
        index += 1
    return counter

# Counts occurrences of the pattern "!=, !=".


def count_neq_neq(sequence):
    index = 0
    counter = 0
    while index < len(sequence) - 2:
        if sequence[index] != sequence[index + 1] != sequence[index + 2]:
            counter += 1
        index += 1
    return counter

# Counts occurrences of a consecutive pattern of inequalities of length 3
# occurs in a sequence.
# Parameters: sequence is a list, symbol1 and symbol2 are strings in
# {'<=','>=','<','>'}
# Returns a count of the number of occurrences of the pattern
# (symbol1, symbol2) in sequence.


def count_ineq3(sequence, symbol1, symbol2):
    if symbol1 == '<=' and symbol2 == '<=':
        return count_leq_leq(sequence)
    elif symbol1 == '<=' and symbol2 == '>=':
        return count_leq_geq(sequence)
    elif symbol1 == '<=' and symbol2 == '<':
        return count_leq_less(sequence)
    elif symbol1 == '<=' and symbol2 == '>':
        return count_leq_great(sequence)
    elif symbol1 == '<=' and symbol2 == '=':
        return count_leq_eq(sequence)
    elif symbol1 == '<=' and symbol2 == '!=':
        return count_leq_neq(sequence)
    elif symbol1 == '>=' and symbol2 == '<=':
        return count_geq_leq(sequence)
    elif symbol1 == '>=' and symbol2 == '>=':
        return count_geq_geq(sequence)
    elif symbol1 == '>=' and symbol2 == '<':
        return count_geq_less(sequence)
    elif symbol1 == '>=' and symbol2 == '>':
        return count_geq_great(sequence)
    elif symbol1 == '>=' and symbol2 == '=':
        return count_geq_eq(sequence)
    elif symbol1 == '>=' and symbol2 == '!=':
        return count_geq_neq(sequence)
    elif symbol1 == '<' and symbol2 == '<=':
        return count_less_leq(sequence)
    elif symbol1 == '<' and symbol2 == '>=':
        return count_less_geq(sequence)
    elif symbol1 == '<' and symbol2 == '<':
        return count_less_less(sequence)
    elif symbol1 == '<' and symbol2 == '>':
        return count_less_great(sequence)
    elif symbol1 == '<' and symbol2 == '=':
        return count_less_eq(sequence)
    elif symbol1 == '<' and symbol2 == '!=':
        return count_less_neq(sequence)
    elif symbol1 == '>' and symbol2 == '<=':
        return count_great_leq(sequence)
    elif symbol1 == '>' and symbol2 == '>=':
        return count_great_geq(sequence)
    elif symbol1 == '>' and symbol2 == '<':
        return count_great_less(sequence)
    elif symbol1 == '>' and symbol2 == '>':
        return count_great_great(sequence)
    elif symbol1 == '>' and symbol2 == '=':
        return count_great_eq(sequence)
    elif symbol1 == '>' and symbol2 == '!=':
        return count_great_neq(sequence)
    elif symbol1 == '=' and symbol2 == '<=':
        return count_eq_leq(sequence)
    elif symbol1 == '=' and symbol2 == '>=':
        return count_eq_geq(sequence)
    elif symbol1 == '=' and symbol2 == '<':
        return count_eq_less(sequence)
    elif symbol1 == '=' and symbol2 == '>':
        return count_eq_great(sequence)
    elif symbol1 == '=' and symbol2 == '=':
        return count_eq_eq(sequence)
    elif symbol1 == '=' and symbol2 == '!=':
        return count_eq_neq(sequence)
    elif symbol1 == '!=' and symbol2 == '<=':
        return count_neq_leq(sequence)
    elif symbol1 == '!=' and symbol2 == '>=':
        return count_neq_geq(sequence)
    elif symbol1 == '!=' and symbol2 == '<':
        return count_neq_less(sequence)
    elif symbol1 == '!=' and symbol2 == '>':
        return count_neq_great(sequence)
    elif symbol1 == '!=' and symbol2 == '=':
        return count_neq_eq(sequence)
    elif symbol1 == '!=' and symbol2 == '!=':
        return count_neq_neq(sequence)
