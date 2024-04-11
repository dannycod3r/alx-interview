#!/usr/bin/python3
"""Pascal's Triangle"""


def pascal_triangle(n):
    """Function returns a list of lists of integers
    representing the Pascal's triangle of n

    Params:
        n (int): height of triangle
    """
    ptri = []  # main list
    if n <= 0:
        return ptri
    else:
        for i in range(n):
            row = [1] * (i + 1)  # 1s
            if i >= 2:
                for j in range(1, i):
                    row[j] = ptri[i - 1][j - 1] + ptri[i - 1][j]
            ptri.append(row)
        return ptri
