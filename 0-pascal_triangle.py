def pascal_triangle(n):
    triangle = []
    if n <= 0:
        return ([])
    else:
        for height in range(n):
            row = []
            for col in range(height + 1):
                if col == 0 or col == height:
                    row.append(1)
                else:
                    row.append(triangle[height - 1][col - 1] +
                               triangle[height - 1][col])
            triangle.append(row)
        return triangle
