from lab04 import *

# Q9
def reverse_iter(lst):
    """Returns the reverse of the given list.

    >>> reverse_iter([1, 2, 3, 4])
    [4, 3, 2, 1]
    """
    "*** YOUR CODE HERE ***"
    lst_len = len(lst)

    for i in range(lst_len//2):
        lst[i], lst[lst_len - i - 1] = lst[lst_len - i - 1], lst[i]

    return lst

#Q6
def merge(lst1, lst2):
    """Merges two sorted lists recursively.

    >>> merge([1, 3, 5], [2, 4, 6])
    [1, 2, 3, 4, 5, 6]
    >>> merge([], [2, 4, 6])
    [2, 4, 6]
    >>> merge([1, 2, 3], [])
    [1, 2, 3]
    >>> merge([5, 7], [2, 4, 6])
    [2, 4, 5, 6, 7]
    """
    "*** YOUR CODE HERE ***"
    if not lst1:
        return lst2
    elif not lst2:
        return lst1
    elif lst1[0] < lst2[0]:
        return [lst1[0]] + merge(lst1[1:], lst2)
    else:
        return [lst2[0]] + merge(lst1, lst2[1:])

# Q10
def mergesort(seq):
    """Mergesort algorithm.

    >>> mergesort([4, 2, 5, 2, 1])
    [1, 2, 2, 4, 5]
    >>> mergesort([])     # sorting an empty list
    []
    >>> mergesort([1])   # sorting a one-element list
    [1]
    """
    "*** YOUR CODE HERE ***"

    if not seq:
        return []
    elif len(seq) == 1:
        return seq
    else:
        seq_len = len(seq)
        left = mergesort(seq[:seq_len//2])
        right = mergesort(seq[seq_len//2:])

        return merge(left, right)

# Q11
def coords(fn, seq, lower, upper):
    """
    >>> seq = [-4, -2, 0, 1, 3]
    >>> fn = lambda x: x**2
    >>> coords(fn, seq, 1, 9)
    [[-2, 4], [1, 1], [3, 9]]
    """ 
    "*** YOUR CODE HERE ***"
    return [[x, fn(x)] for x in seq if fn(x) in range(lower, upper+1)]

# Q12
def deck(suits, numbers):
    """Creates a deck of cards (a list of 2-element lists) with the given
    suits and numbers. Each element in the returned list should be of the form
    [suit, number].

    >>> deck(['S', 'C'], [1, 2, 3])
    [['S', 1], ['S', 2], ['S', 3], ['C', 1], ['C', 2], ['C', 3]]
    >>> deck(['S', 'C'], [3, 2, 1])
    [['S', 3], ['S', 2], ['S', 1], ['C', 3], ['C', 2], ['C', 1]]
    >>> deck([], [3, 2, 1])
    []
    >>> deck(['S', 'C'], [])
    []
    """
    "*** YOUR CODE HERE ***"
    if not suits or not numbers:
        return []

    return [[s, n] for s in suits for n in numbers]

# Q13
def add_matrices(x, y):
    """
    >>> matrix1 = [[1, 3],
    ...            [2, 0]]
    >>> matrix2 = [[-3, 0],
    ...            [1, 2]]
    >>> add_matrices(matrix1, matrix2)
    [[-2, 3], [3, 2]]
    """
    "*** YOUR CODE HERE ***"
    return [[x[i][j] + y[i][j] for i in range(len(x))] for j in range(len(y))]

