import sympy as sym
from math import sqrt

def gen_expansion(n, prec):
    """ Generate an arbitrary large decimal expansion for a mathematical expression.
    
    Parameters:
    -----------
    
    n : SymPy expressions
        An exact SymPy mathematical expression.
    prec: int
        Precision required.
    
    Returns
    -------
    str
    A string of the decimal expansion with the specified precision.
    """
    # check if the precision number makes sense
    if prec <= 0:
        raise ValueError("Precision should be an positive integer.")
    elif type(prec) != int:
        raise ValueError("Precision should be an positive integer.")
    
    # obtain the math expression up to specified floating point precision
    nf = n.evalf(prec)
    
    # get the decimal expansion by splitting 
    # only get the first halbf of the split
    splited1, _ = str(nf).split('.')
    
    # check how many digits are to the left of .
    # modified the precision value to get the exact precision value specified 
    prec2 = prec + len(splited1)
    
    # repeat the steps to obtain the number with updated precision
    # return the str version of the floating number
    return str(n.evalf(prec2)).split('.')[1]

def is_prime(n):
    
    """ Check whether a number is a prime number.
    
    Parameters:
    -----------
    
    n : int
        The number to be checked for whether it is a prime number.
    
    Returns
    -------
    bool
    Return True if it is a prime number, else, return False.
    """
    if type(n) != int:
        raise TypeError("Input must be a positive integer.")
    elif n < 0:
        raise ValueError("Input must be a positive integer.")
    # initiate a flag to indicate whether a factor has found
    flag = 0
    
    # special case: 0 and 1 are not prime number.
    if (n == 0) | (n == 1):
        flag = 1
    
    # iterate through all number between 2 and sqrt(n)
    for i in range(2, int(sqrt(n)) + 1):
        
        # if a factor of n has been found
        if (n%i == 0):
            
            # n is not a prime number - search if over
            flag = 1
            # break out the for loop 
            break
            
    # if a factor has found during the for-loop, return False for prime number         
    if flag == 1:
        return False
    # else, number n is a prime number
    else:
        return True
        
def sliding_window(seq, window_size):
    """
    Generate sliding windows of a specified width from a long iterable.
    
    Parameters
    ----------
    seq : str
            a string of number to be iterated.

    window_size : int
            Sliding window size.
    
    Returns
    -------
    List
    Sliding window integers from specified window size. Strings starts from 0 are removed.
    
    """
    
    if type(seq) != str:
        raise AttributeError("Input Sequence must be string type.")
    elif type(window_size) != int:
        raise AttributeError("Window size must be int type.")
    elif window_size <=0:
        raise ValueError("Window size must be a postive integer.")
    elif len(seq) <= window_size:
        raise ValueError("The sequence must be longer than the window size.")
    
    # get the length of the large number.
    # in this case, it is the precision specified in the previous function
    prec = len(seq)
    
    # calculate the size of the list for all numbers after the sliding window 
    list_len = prec - window_size + 1
    
    # initiate a list with specified length
    breaks = [None] * list_len
    
    # iterate through the initiated list
    for s in range(0, list_len):
        # update the end of indexing according to the window size
        e = s + window_size
        
        # index the string 
        breaks[s] = seq[s:e]
        
    # remove any string that starts with 0 - not number with desired numbers of digits
    windowed_l = [int(s) for s in breaks if s[0] != '0']
    
    return windowed_l

def main(n, prec, window_size):
    """Calls all sub-functions to produce the first 10-digit prime in the a mathematical expression.
    
    Parameters
    ----------
    n : 
        A mathematical expression to be evaluated.
        
    prec : int
        Precision desired.
    
    window_size : int
        Sliding window size.
    
    Returns
    -------
    int
    The first 10-digit prime number.

    """
    # get the decimal expansion
    l_num = gen_expansion(n, prec)
    
    # get a list of sub-numbers with specified number of digit
    window_list = sliding_window(l_num, window_size)
    
    # for each number in the list,
    # check if it is a prime number 
    for w in window_list:
        
        # if prime number is found
        if is_prime(w):
            
            # search is over - break out the loop
            break
    # return the number
    return w
