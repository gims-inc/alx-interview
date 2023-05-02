#!/usr/bin/python3
"""
The minimum operations coding solution.
"""


def minOperations(n: int) -> int:
    """Computes the least number of operations needed to result
    in exactly n H characters.

    args:
        n: (int) Target number
    Returns: (int) Number of operations

    """
    ops = 0
    min_ops = 2
    while n > 1:
        if n % min_ops == 0:
            ops += min_ops
            n /= min_ops
        else:
            min_ops += 1
    return ops
