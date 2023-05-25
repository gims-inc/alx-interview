# Island_perimeter

## Task

Create a function def island_perimeter(grid): that returns the perimeter of the island described in grid:

    grid is a list of list of integers:
        0 represents water
        1 represents land
        Each cell is square, with a side length of 1
        Cells are connected horizontally/vertically (not diagonally).
        grid is rectangular, with its width and height not exceeding 100
    The grid is completely surrounded by water
    There is only one island (or nothing).
    The island doesn’t have “lakes” (water inside that isn’t connected to the water surrounding the island).

## soln

In the problem, the island is typically represented by a grid, where each cell can either be land or water. Land cells are usually denoted by "1," and water cells are denoted by "0." The island's shape can vary, but it is usually connected, without any isolated land masses within it.

To calculate the perimeter of the island, you need to consider the edges of the grid and the adjacent cells surrounding the land cells. For each land cell, you count the number of neighboring cells that are either water cells or grid edges. The sum of these counts gives you the perimeter of the island.

There are various approaches to solving this problem, including recursive algorithms, breadth-first search (BFS), or depth-first search (DFS) techniques. The specific solution may depend on the programming language or environment you are using.
