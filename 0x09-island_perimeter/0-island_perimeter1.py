#!/usr/bin/python3
"""grid is a list of list of integers:

    0 represents water
    1 represents land
    Each cell is square, with a side length of 1
    Cells are connected horizontally/vertically (not diagonally).
    grid is rectangular, with its width and height not exceeding 100
"""

def island_perimeter(grid):
    """
    Returns the perimeter of the islands in the given grid.
    
    Args:
        grid (list): A list of lists representing the grid.
        
    Returns:
        int: The perimeter of the islands.
    """
    width = len(grid[0])
    height = len(grid)
    perimeter = 0

    for i in range(height):
        for j in range(width):
            if grid[i][j] == 1:
                perimeter += count_neighbors(grid, i, j)

    return perimeter


def count_neighbors(grid, i, j):
    """
    Counts the number of neighboring cells that contribute to the perimeter.
    
    Args:
        grid (list): A list of lists representing the grid.
        i (int): The row index of the current cell.
        j (int): The column index of the current cell.
        
    Returns:
        int: The count of neighboring cells that contribute to the perimeter.
    """
    width = len(grid[0])
    height = len(grid)
    count = 0

    # Check left neighbor
    if j == 0 or grid[i][j - 1] == 0:
        count += 1

    # Check right neighbor
    if j == width - 1 or grid[i][j + 1] == 0:
        count += 1

    # Check top neighbor
    if i == 0 or grid[i - 1][j] == 0:
        count += 1

    # Check bottom neighbor
    if i == height - 1 or grid[i + 1][j] == 0:
        count += 1

    return count
