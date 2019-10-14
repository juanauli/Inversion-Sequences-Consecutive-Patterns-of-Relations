# Tests for functions from the files:
# CONSEC_INEQ3.py
# COUNT_OCCUR_CONSEC_INEQ3.py

from CONSEC_INEQ3 import count_inv_avoiding_ineq3
from CONSEC_INEQ3 import find_inv_avoiding_ineq3
from COUNT_OCCUR_CONSEC_INEQ3 import occur_ineq3
from COUNT_OCCUR_CONSEC_INEQ3 import occur_list_ineq3

# Remark: The symbols are entered as strings. The possible strings are '<=',
# '>=', '<', '>', '=' and '!='

# Count inversion sequences avoiding a pattern of inequalities
# print count_inv_avoiding_ineq3(10, '<=', '<')

# Find inversion sequences avoiding a pattern of inequalities
# print find_inv_avoiding_ineq3(4, '<', '!=')

# Count occurrences of a pattern inequalities amont inversion sequences
# print occur_ineq3(3, '!=', '>=')

# Find occurrences of a pattern inequalities amont inversion sequences
# print occur_list_ineq3(3, '<', '<=')
