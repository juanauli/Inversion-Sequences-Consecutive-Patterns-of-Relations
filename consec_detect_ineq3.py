# Detection of consecutive patterns of inequalities of length 3

# Detects the pattern "<=, <=".


def detect_leq_leq(sequence):
    index = 0
    while index < len(sequence) - 2:
        if sequence[index] <= sequence[index + 1] <= sequence[index + 2]:
            return True
        index += 1
    return False

# Detects the pattern "<=, >=".


def detect_leq_geq(sequence):
    index = 0
    while index < len(sequence) - 2:
        if sequence[index] <= sequence[index + 1] >= sequence[index + 2]:
            return True
        index += 1
    return False

# Detects the pattern "<=, <".


def detect_leq_less(sequence):
    index = 0
    while index < len(sequence) - 2:
        if sequence[index] <= sequence[index + 1] < sequence[index + 2]:
            return True
        index += 1
    return False

# Detects the pattern "<=, >".


def detect_leq_great(sequence):
    index = 0
    while index < len(sequence) - 2:
        if sequence[index] <= sequence[index + 1] > sequence[index + 2]:
            return True
        index += 1
    return False

# Detects the pattern "<=, =".


def detect_leq_eq(sequence):
    index = 0
    while index < len(sequence) - 2:
        if sequence[index] <= sequence[index + 1] == sequence[index + 2]:
            return True
        index += 1
    return False

# Detects the pattern "<=, !=".


def detect_leq_neq(sequence):
    index = 0
    while index < len(sequence) - 2:
        if sequence[index] <= sequence[index + 1] != sequence[index + 2]:
            return True
        index += 1
    return False

# Detects the pattern ">=, <=".


def detect_geq_leq(sequence):
    index = 0
    while index < len(sequence) - 2:
        if sequence[index] >= sequence[index + 1] <= sequence[index + 2]:
            return True
        index += 1
    return False

# Detects the pattern ">=, >=".


def detect_geq_geq(sequence):
    index = 0
    while index < len(sequence) - 2:
        if sequence[index] >= sequence[index + 1] >= sequence[index + 2]:
            return True
        index += 1
    return False

# Detects the pattern ">=, <".


def detect_geq_less(sequence):
    index = 0
    while index < len(sequence) - 2:
        if sequence[index] >= sequence[index + 1] < sequence[index + 2]:
            return True
        index += 1
    return False

# Detects the pattern ">=, >".


def detect_geq_great(sequence):
    index = 0
    while index < len(sequence) - 2:
        if sequence[index] >= sequence[index + 1] > sequence[index + 2]:
            return True
        index += 1
    return False

# Detects the pattern ">=, =".


def detect_geq_eq(sequence):
    index = 0
    while index < len(sequence) - 2:
        if sequence[index] >= sequence[index + 1] == sequence[index + 2]:
            return True
        index += 1
    return False

# Detects the pattern ">=, !=".


def detect_geq_neq(sequence):
    index = 0
    while index < len(sequence) - 2:
        if sequence[index] >= sequence[index + 1] != sequence[index + 2]:
            return True
        index += 1
    return False

# Detects the pattern "<, <=".


def detect_less_leq(sequence):
    index = 0
    while index < len(sequence) - 2:
        if sequence[index] < sequence[index + 1] <= sequence[index + 2]:
            return True
        index += 1
    return False


# Detects the pattern "<, >=".


def detect_less_geq(sequence):
    index = 0
    while index < len(sequence) - 2:
        if sequence[index] < sequence[index + 1] >= sequence[index + 2]:
            return True
        index += 1
    return False

# Detects the pattern "<, <".


def detect_less_less(sequence):
    index = 0
    while index < len(sequence) - 2:
        if sequence[index] < sequence[index + 1] < sequence[index + 2]:
            return True
        index += 1
    return False

# Detects the pattern "<, >".


def detect_less_great(sequence):
    index = 0
    while index < len(sequence) - 2:
        if sequence[index] < sequence[index + 1] > sequence[index + 2]:
            return True
        index += 1
    return False

# Detects the pattern "<, =".


def detect_less_eq(sequence):
    index = 0
    while index < len(sequence) - 2:
        if sequence[index] < sequence[index + 1] == sequence[index + 2]:
            return True
        index += 1
    return False

# Detects the pattern "<, !=".


def detect_less_neq(sequence):
    index = 0
    while index < len(sequence) - 2:
        if sequence[index] < sequence[index + 1] != sequence[index + 2]:
            return True
        index += 1
    return False

# Detects the pattern ">, <=".


def detect_great_leq(sequence):
    index = 0
    while index < len(sequence) - 2:
        if sequence[index] > sequence[index + 1] <= sequence[index + 2]:
            return True
        index += 1
    return False

# Detects the pattern ">, >=".


def detect_great_geq(sequence):
    index = 0
    while index < len(sequence) - 2:
        if sequence[index] > sequence[index + 1] >= sequence[index + 2]:
            return True
        index += 1
    return False

# Detects the pattern ">, <".


def detect_great_less(sequence):
    index = 0
    while index < len(sequence) - 2:
        if sequence[index] > sequence[index + 1] < sequence[index + 2]:
            return True
        index += 1
    return False

# Detects the pattern ">, >".


def detect_great_great(sequence):
    index = 0
    while index < len(sequence) - 2:
        if sequence[index] > sequence[index + 1] > sequence[index + 2]:
            return True
        index += 1
    return False

# Detects the pattern ">, =".


def detect_great_eq(sequence):
    index = 0
    while index < len(sequence) - 2:
        if sequence[index] > sequence[index + 1] == sequence[index + 2]:
            return True
        index += 1
    return False

# Detects the pattern ">, !=".


def detect_great_neq(sequence):
    index = 0
    while index < len(sequence) - 2:
        if sequence[index] > sequence[index + 1] != sequence[index + 2]:
            return True
        index += 1
    return False

# Detects the pattern "=, <=".


def detect_eq_leq(sequence):
    index = 0
    while index < len(sequence) - 2:
        if sequence[index] == sequence[index + 1] <= sequence[index + 2]:
            return True
        index += 1
    return False

# Detects the pattern "=, >=".


def detect_eq_geq(sequence):
    index = 0
    while index < len(sequence) - 2:
        if sequence[index] == sequence[index + 1] >= sequence[index + 2]:
            return True
        index += 1
    return False

# Detects the pattern "=, <".


def detect_eq_less(sequence):
    index = 0
    while index < len(sequence) - 2:
        if sequence[index] == sequence[index + 1] < sequence[index + 2]:
            return True
        index += 1
    return False

# Detects the pattern "=, >".


def detect_eq_great(sequence):
    index = 0
    while index < len(sequence) - 2:
        if sequence[index] == sequence[index + 1] > sequence[index + 2]:
            return True
        index += 1
    return False

# Detects the pattern "=, =".


def detect_eq_eq(sequence):
    index = 0
    while index < len(sequence) - 2:
        if sequence[index] == sequence[index + 1] == sequence[index + 2]:
            return True
        index += 1
    return False

# Detects the pattern "=, !=".


def detect_eq_neq(sequence):
    index = 0
    while index < len(sequence) - 2:
        if sequence[index] == sequence[index + 1] != sequence[index + 2]:
            return True
        index += 1
    return False

# Detects the pattern "!=, <=".


def detect_neq_leq(sequence):
    index = 0
    while index < len(sequence) - 2:
        if sequence[index] != sequence[index + 1] <= sequence[index + 2]:
            return True
        index += 1
    return False

# Detects the pattern "!=, >=".


def detect_neq_geq(sequence):
    index = 0
    while index < len(sequence) - 2:
        if sequence[index] != sequence[index + 1] >= sequence[index + 2]:
            return True
        index += 1
    return False

# Detects the pattern "!=, <".


def detect_neq_less(sequence):
    index = 0
    while index < len(sequence) - 2:
        if sequence[index] != sequence[index + 1] < sequence[index + 2]:
            return True
        index += 1
    return False

# Detects the pattern "!=, >".


def detect_neq_great(sequence):
    index = 0
    while index < len(sequence) - 2:
        if sequence[index] != sequence[index + 1] > sequence[index + 2]:
            return True
        index += 1
    return False

# Detects the pattern "!=, =".


def detect_neq_eq(sequence):
    index = 0
    while index < len(sequence) - 2:
        if sequence[index] != sequence[index + 1] == sequence[index + 2]:
            return True
        index += 1
    return False

# Detects the pattern "!=, !=".


def detect_neq_neq(sequence):
    index = 0
    while index < len(sequence) - 2:
        if sequence[index] != sequence[index + 1] != sequence[index + 2]:
            return True
        index += 1
    return False

# Determines if a pattern of inequalities of length 3 occurs in a sequence.
# Parameters: sequence is a list, symbol1 and symbol2 are strings in
# {'<=','>=','<','>'}
# Returns True if the pattern is found and False otherwise.


def detect_ineq3(sequence, symbol1, symbol2):
    if symbol1 == '<=' and symbol2 == '<=':
        return detect_leq_leq(sequence)
    elif symbol1 == '<=' and symbol2 == '>=':
        return detect_leq_geq(sequence)
    elif symbol1 == '<=' and symbol2 == '<':
        return detect_leq_less(sequence)
    elif symbol1 == '<=' and symbol2 == '>':
        return detect_leq_great(sequence)
    elif symbol1 == '<=' and symbol2 == '=':
        return detect_leq_eq(sequence)
    elif symbol1 == '<=' and symbol2 == '!=':
        return detect_leq_neq(sequence)
    elif symbol1 == '>=' and symbol2 == '<=':
        return detect_geq_leq(sequence)
    elif symbol1 == '>=' and symbol2 == '>=':
        return detect_geq_geq(sequence)
    elif symbol1 == '>=' and symbol2 == '<':
        return detect_geq_less(sequence)
    elif symbol1 == '>=' and symbol2 == '>':
        return detect_geq_great(sequence)
    elif symbol1 == '>=' and symbol2 == '=':
        return detect_geq_eq(sequence)
    elif symbol1 == '>=' and symbol2 == '!=':
        return detect_geq_neq(sequence)
    elif symbol1 == '<' and symbol2 == '<=':
        return detect_less_leq(sequence)
    elif symbol1 == '<' and symbol2 == '>=':
        return detect_less_geq(sequence)
    elif symbol1 == '<' and symbol2 == '<':
        return detect_less_less(sequence)
    elif symbol1 == '<' and symbol2 == '>':
        return detect_less_great(sequence)
    elif symbol1 == '<' and symbol2 == '=':
        return detect_less_eq(sequence)
    elif symbol1 == '<' and symbol2 == '!=':
        return detect_less_neq(sequence)
    elif symbol1 == '>' and symbol2 == '<=':
        return detect_great_leq(sequence)
    elif symbol1 == '>' and symbol2 == '>=':
        return detect_great_geq(sequence)
    elif symbol1 == '>' and symbol2 == '<':
        return detect_great_less(sequence)
    elif symbol1 == '>' and symbol2 == '>':
        return detect_great_great(sequence)
    elif symbol1 == '>' and symbol2 == '=':
        return detect_great_eq(sequence)
    elif symbol1 == '>' and symbol2 == '!=':
        return detect_great_neq(sequence)
    elif symbol1 == '=' and symbol2 == '<=':
        return detect_eq_leq(sequence)
    elif symbol1 == '=' and symbol2 == '>=':
        return detect_eq_geq(sequence)
    elif symbol1 == '=' and symbol2 == '<':
        return detect_eq_less(sequence)
    elif symbol1 == '=' and symbol2 == '>':
        return detect_eq_great(sequence)
    elif symbol1 == '=' and symbol2 == '=':
        return detect_eq_eq(sequence)
    elif symbol1 == '=' and symbol2 == '!=':
        return detect_eq_neq(sequence)
    elif symbol1 == '!=' and symbol2 == '<=':
        return detect_neq_leq(sequence)
    elif symbol1 == '!=' and symbol2 == '>=':
        return detect_neq_geq(sequence)
    elif symbol1 == '!=' and symbol2 == '<':
        return detect_neq_less(sequence)
    elif symbol1 == '!=' and symbol2 == '>':
        return detect_neq_great(sequence)
    elif symbol1 == '!=' and symbol2 == '=':
        return detect_neq_eq(sequence)
    elif symbol1 == '!=' and symbol2 == '!=':
        return detect_neq_neq(sequence)
