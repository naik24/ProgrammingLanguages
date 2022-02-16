squares = [1, 4, 9, 16, 25]

# Indexing Lists
for i in range(len(squares)):
    print(squares[i])

"""
The last element of a list is also indexed as -1, the second last element as -2, and so on.
"""
print(squares[-1])

# Splicing Lists
print(squares[0:3])

# Concatenating Lists
print(squares + [36, 49, 64, 81, 100])
