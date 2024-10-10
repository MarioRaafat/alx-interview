#!/usr/bin/python3
"""
This module contains a function that calculates the perimeter of an island
defined in a grid. The grid is represented as a list of lists of integers,
where 0 represents water and 1 represents land.
"""

def island_perimeter(grid):
    """
    Calculate the perimeter of an island represented in the grid.
    
    Args:
        grid (list): A list of lists of integers, where 0 represents water
                     and 1 represents land. The grid is completely surrounded
                     by water, and the island is connected horizontally/vertically.
    
    Returns:
        int: The perimeter of the island in the grid.
    """
    perimeter = 0
    rows = len(grid)
    cols = len(grid[0])

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1:
                # Add 4 for each land cell
                perimeter += 4

                if i > 0 and grid[i-1][j] == 1:  # Check the cell above
                    perimeter -= 2
                if j > 0 and grid[i][j-1] == 1:  # Check the cell to the left
                    perimeter -= 2
    return perimeter
