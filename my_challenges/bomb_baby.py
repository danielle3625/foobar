import itertools as it
import sys

def back_step(tup,i):
    a = tup[0]
    b = tup[1]
    if a < 1 or b < 1 or (max((a,b))%min((a,b)) == 0 and min((a,b)) != 1): #impossible
        return (-1,-1),i
    if a >= b:
        return (a-b*((a-1)//b),b),i + ((a-1)//b)    # Should've documented better, because I don't remember this well :DD
    else:
        return (a,b-a*((b-1)//a)), i + ((b-1)//a)

def solution(M,F):
    """Returns the smallest amount of iterations required to reach the pair (M,F)
    starting from (1,1).
    Iterating from (1,1)  forwards: in every step there are two possible next iterations: (a1,a2) -> (a1+a2, a2) and (a1,a1+a2).
    If there is no amount of iterations that would yield the desired pair (M,N), returns the string 'impossible'.
    For example:
    Given the pair (4,7):
    because 7>4 we know the previous step must've been (4, 3) -> then (1,3) -> (1,2) -> (1,1): Hence 4 steps to reach (1,1)
    Args:
        M (str): an integer up to 10**50
        F (str): an integer up to 10**50

    Returns:
        str: iterations
    """    
    M = int(M)
    F = int(F)
    i = 0
    target_sum = sum((M,F))
    step = (M,F)
    while step != (1,1) and step != (-1,-1):
        step,i = back_step(step,i)
    if step != (1,1):
        return "impossible"
    return str(i)

