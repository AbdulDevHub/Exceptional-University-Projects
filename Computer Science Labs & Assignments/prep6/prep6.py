"""Prep 6 Synthesize

=== CSC148 Winter 2022 ===
Department of Mathematical and Computational Sciences,
University of Toronto Mississauga

=== Module Description ===
Your task in this prep is to implement each of the following recursive functions
on nested lists, using the following steps for *Recursive Function Design*:

1.  Identify the recursive structure of the input (in this case, always a nested
    list), and write down the code template for nested lists:

    def f(obj: Union[int, list]) -> ...:
        if isinstance(obj, int):
            ...
        else:
            ...
            for sublist in obj:
                ... f(sublist) ...
            ...

2.  Implement the base case(s) directly (in this case, a single integer).
3.  Write down a concrete example with a somewhat complex argument, (in this
    case, a nested list with around 3 sub-nested-lists), and then write down
    the relevant recursive calls and what they should return.
4.  Determine how to combine the recursive calls to compute the correct output.
    Make sure you can express this in English first, and then implement your
    idea.

HINT: The implementations here should be similar to ones you've seen
before in the readings or comprehension questions.
"""
from typing import Union


def num_positives(obj: Union[int, list]) -> int:
    """Return the number of positive integers in <obj>.

    Remember, 0 is *not* positive.

    >>> num_positives(17)
    1
    >>> num_positives(-10)
    0
    >>> num_positives([1, -2, [-10, 2, [3], 4, -5], 4])
    5
    >>> num_positives([1, -2, -10, 2, 3, 4, -5, 4])
    5
    >>> num_positives([])
    0
    >>> num_positives([[[]],[[]],[]])
    0
    >>> num_positives([5, -5, 0, [5, 10, -15, [0], 1],[-1, [4]],[], [[[[[]]]]]])
    5
    """
    if isinstance(obj, int):
        if obj > 0:
            return 1
        return 0
    else:
        counter = 0
        for sublist in obj:
            num = num_positives(sublist)
            counter += num
        return counter


def nested_max(obj: Union[int, list]) -> int:
    """Return the maximum integer stored in nested list <obj>.

    Return 0 if <obj> is an empty list.

    Precondition: all integers in <obj> are positive.

    >>> nested_max(17)
    17
    >>> nested_max([1, 2, [1, 2, [3], 4, 5], 4])
    5
    >>> nested_max([1, 1, [1, 1, [1], 1, 1], 1])
    1
    >>> nested_max([1, 2, 10, 2, 3, 4, 5, 4])
    10
    >>> nested_max([])
    0
    >>> nested_max([[[]],[[]],[]])
    0
    >>> nested_max([5, 5, 0, [5, 10, 15, [4], 1],[1, [4]],[], [[[[[16]]]]]])
    16
    """
    if isinstance(obj, int):
        return obj
    else:
        max_num = 0
        for sublist in obj:
            num = nested_max(sublist)
            max_num = max(num, max_num)
        return max_num


def max_length(obj: Union[int, list]) -> int:
    """Return the maximum length of any list in nested list <obj>.

    The *maximum length* of a nested list is defined as:
    1. 0, if <obj> is a number.
    2. The maximum of len(obj) and the lengths of the nested lists contained
       in <obj>, if <obj> is a list.

    >>> max_length(17)
    0
    >>> max_length([1, 2, [1, 2], 4])
    4
    >>> max_length([1, 2, [1, 2, [3], 4, 5], 4])
    5
    >>> max_length([1, 1, [1, 1, [1], 1, 1], 1])
    5
    >>> max_length([1, 2, 10, 2, 3, 4, 5, 4])
    8
    >>> max_length([])
    0
    >>> max_length([[[]],[[]],[]])
    3
    >>> max_length([5, 5, 0, [5, 10, 15, [4], 1],[1, [4]],[], [[[[[], [[]]]]]]])
    7
    >>> max_length([5, 5, 0, [5, 10, 15, [4], 1, 5, 45, 4], [1, [4], [4]]])
    8
    >>> max_length([5, [5, 10, 15, [4], 1, 5], [1, [4, [1, 1, 1, 1, 1, 1, 1]]]])
    7
    """
    if isinstance(obj, int):
        return 0
    else:
        max_len = len(obj)
        for sublist in obj:
            lst = max_length(sublist)
            max_len = max(max_len, lst)
        return max_len


if __name__ == '__main__':
    import doctest
    doctest.testmod()

    import python_ta
    python_ta.check_all()
