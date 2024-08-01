#!/usr/bin/python3
"""Supplies function that return the perimeter of island
"""


def island_perimeter(grid):
    """
    Returns the perimeter of the island described in the grid.

    :param grid: List[List[int]] - A list of lists where 0 represents
     water and 1 represents land.
    :return: int - The perimeter of the island.
    """
    perimeter = 0
    rows = len(grid)
    cols = len(grid[0]) if rows > 0 else 0

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 1:
                # Check each of the four sides
                if r == 0 or grid[r - 1][c] == 0:  # Up
                    perimeter += 1
                if r == rows - 1 or grid[r + 1][c] == 0:  # Down
                    perimeter += 1
                if c == 0 or grid[r][c - 1] == 0:  # Left
                    perimeter += 1
                if c == cols - 1 or grid[r][c + 1] == 0:  # Right
                    perimeter += 1

    return perimeter
