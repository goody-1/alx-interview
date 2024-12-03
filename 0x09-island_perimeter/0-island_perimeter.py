#!/usr/bin/python3
"""
Get the perimeter of an island in a grid
"""


def island_perimeter(grid):
    """
    Calculate the perimeter of the island described in grid.

    :param grid: List[List[int]], the grid representation of the island
    :return: int, the perimeter of the island
    """
    perimeter = 0
    rows = len(grid)
    cols = len(grid[0]) if rows > 0 else 0

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 1:  # Land cell
                # Start with 4 sides for each land cell
                perimeter += 4

                # Subtract sides for neighboring land cells
                if r > 0 and grid[r - 1][c] == 1:  # Check above
                    perimeter -= 2
                if c > 0 and grid[r][c - 1] == 1:  # Check left
                    perimeter -= 2
    return perimeter
