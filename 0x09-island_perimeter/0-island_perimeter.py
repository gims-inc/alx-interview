#!/usr/bin/python3
"""grid is a list of list of integers:

    0 represents water
    1 represents land
    Each cell is square, with a side length of 1
    Cells are connected horizontally/vertically (not diagonally).
    grid is rectangular, with its width and height not exceeding 100
"""


def count_adjacent_edges(grid, i, j):
    """
    Counts the number of adjacent edges around a land cell in the grid.

    Args:
        grid (list): A list of lists representing the grid.
        i (int): The row index of the land cell.
        j (int): The column index of the land cell.

    Returns:
        int: The count of adjacent edges.
    """
    count = 0
    if j > 0 and grid[i][j - 1] == 1:
        count += 1
    if i > 0 and grid[i - 1][j] == 1:
        count += 1
    # Check other adjacent cells if needed

    return count


def island_perimeter(grid):
    """
    Returns the perimeter of the islands in the given grid.
 
    Args:
        grid (list): A list of lists representing the grid.

    Returns:
        int: The perimeter of the islands.
    """
    if type(grid) != list:
        return 0

    width, height = len(grid[0]), len(grid)
    edges, size = 0, 0

    for i in range(height):
        for j in range(width):
            if grid[i][j] == 1:
                size += 1
                edges += count_adjacent_edges(grid, i, j)

    return size * 4 - edges * 2
