# List of squares
squares = [x**2 for x in range(1,11)]
print(squares)

# Even squares
even_squares = [y for y in squares if y % 2 == 0]
print(even_squares)

# Nested List Comprehension
matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12]
    ]

"""
Following list comprehension will transpose the rows and columns
"""
transpose = [[row[i] for row in matrix] for i in range(4)]
print(transpose)
