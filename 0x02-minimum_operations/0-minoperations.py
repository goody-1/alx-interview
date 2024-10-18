#!/usr/bin/python3
"""Module containing the function that calcuates the minimum
number of operations (Copy All and Paste) need to get the exact
number of characters or text in a file.

--- IDEA ---
In a text file, there is a single character H. Your text editor can
execute only two operations in this file: Copy All and Paste.
Given a number n, this method calculates the fewest number of operations
needed to result in exactly n H characters in the file.

Prototype: def minOperations(n)
Returns an integer
If n is impossible to achieve, return 0
Example:

n = 9

H => Copy All => Paste => HH => Paste =>HHH => Copy All => Paste =>
HHHHHH => Paste => HHHHHHHHH

Number of operations: 6
"""


def minOperations(n):
    """Retuns and integer - the minimum number of operations"""
    if n <= 1:
        return 0

    operations = 0
    factor = 2

    while n > 1:
        # Check if current factor divides n
        while n % factor == 0:
            operations += factor
            n //= factor
        factor += 1

    return operations
