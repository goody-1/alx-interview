#!/usr/bin/python3
"""This module contains a function that prints the Pascal triangle"""


def pascal_triangle(n):
    """
    Returns a list of lists of integers representing the \
    Pascal's triangle of n
    """

    if n <= 0:
        return []
    triangle = [[1]]

    if n == 1:
        return triangle
    triangle.append([1, 1])
    if n == 2:
        return triangle

    for i in range(2, n):
        cur_triangle = triangle[-1]
        cur_row = []

        for j in range(len(cur_triangle) - 1):
            cur_row.append(cur_triangle[j] + cur_triangle[j + 1])
        cur_row = [1] + cur_row + [1]

        triangle.append(cur_row)

    return triangle
