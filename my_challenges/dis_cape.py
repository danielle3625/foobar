import math
from fractions import Fraction, gcd
from collections import Counter

def solution(w,h,s):
    """
    Return the number of non-equivalent (https://en.wikipedia.org/wiki/Matrix_equivalence) 
    matrices with dimensions w x h, and s different possible values.
    
    This is the same as the number of orbits (https://en.wikipedia.org/wiki/Group_action#Orbits_and_stabilizers)
    for the action group G (all different row and column switches)
    acting on set X (all different matrices filling the restrictions).
    
    This in turn is the same as the average number of fixed points (https://en.wikipedia.org/wiki/Group_action#Fixed_points_and_stabilizer_subgroups)
    for the action group G acting on set X.
    """
    ans = 0
    row_cycle_vectors = get_cycle_vectors(h)    # Get the cycle vectors and their coefficients
    col_cycle_vectors = get_cycle_vectors(w)
    # Loop through all row and column cycles
    for rc_vec,r_coef in row_cycle_vectors.items():
        for cc_vec,c_coef in col_cycle_vectors.items():
            coeff = r_coef*c_coef
            combined_vec = combine(rc_vec,cc_vec)
            value = 1
            # Combine the cycle indices and calculate cycle index of the cartesian product of the cycles
            for _, power in combined_vec:
                value *= s ** power
            ans += coeff * value
    return str(int(ans))

def combine(a_cycles, b_cycles):
    """
    Combine the row cycles and the column cycles according to this formula:
    https://math.stackexchange.com/questions/2113657/burnsides-lemma-applied-to-grids-with-interchanging-rows-and-columns/2343500#2343500.
    len_ tells the length of the cycle
    freg_ tells the frequency of len_ subcycles in _cycles
    """
    combined = []
    for len_a, freq_a in enumerate(a_cycles):
        len_a += 1      # Add one because len_ != 0
        for len_b, freq_b in enumerate(b_cycles):
            len_b += 1
            lcm = (len_a * len_b) / gcd(len_a, len_b)   # Calculate least-common multiple
            combined.append((lcm, int(len_a * freq_a * len_b * freq_b / lcm)))
    return combined
    
def partitions(n):
    """
    Recursively yield the partitions of n as a list of the components (each list sums to n).
    """
	# base case
    if n == 0:
        yield []
        return
    # get partitions of n-1
    for p in partitions(n-1):
        yield [1] + p
        if p and (len(p) < 2 or p[1] > p[0]):
            yield [p[0] + 1] + p[1:]

def get_cycle_vectors(n):
    """
    https://en.wikipedia.org/wiki/Cycle_index#Disjoint_cycle_representation_of_permutations
    Return the unique cycles of an array of length n (conjugacy classes, which are partitions of integer n),
    and the corresponding coefficients for the cycle index.
    Returned as a dictionary with unique_cycle : coefficient -pairs.
    The cycles are encoded so that, the index(+1) denotes the length of the subcycle
    and the value at the index(+1) denotes the number of such type cycles (same length).
    Kind of like one-hot encoded vectors.
    
    Each member in the dictionary then essentially holds the dummy variable of a cycle of disctinct length (the cycle indexes term) and its coefficient.
    """
    vectors = partitions(n) # Get the distinct cycles (conjugacy classes), which are the partitions: https://en.wikipedia.org/wiki/Symmetric_group#Conjugacy_classes
    J = {}
    for v in vectors:
        base = [0 for _ in range(n)]
        c = Counter(v)
        for item, count in c.items():
            base[item-1] += count   # Modfiy base vector, leaving 0 as val
        J[tuple(base)] = coefficient_of_cycle(base)
    return J

def coefficient_of_cycle(j):
    """
    Return the coefficient of a cycle j according to a formula for counting it.
    It is the inner part of the formula for the cycle index, found here: https://en.wikipedia.org/wiki/Cycle_index#Symmetric_group_Sn
    Returns it as Fraction instance for higher accuracy.
    """
    # in j, index + 1 is the length of the subcycle and the value at index is the number of times the subcycle is repeated in the cycle.
    s = 1
    for n in range(1,len(j)+1):
        s *= math.factorial(j[n-1])*n**j[n-1]
    return Fraction(1,s)

