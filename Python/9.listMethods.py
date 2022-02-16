# Sample List
l = [10, 70, 30, 90, 50]

# Appending to list
l.append(60)
print("Append:", l)

# Extending the list
l.extend([70, 80, 90, 100])
print("Extend:", l)

# Inserting into list
l.insert(len(l), 110)
print("Insert:", l)

# Removing from list
l.remove(110)
print("Remove:", l)

# Pop
l_pop = l.pop()
print("Pop:", l_pop)

# Finding the index of an element
pos = l.index(70)
print("Index:", pos)

#Counting number of occurences of an element
cnt = l.count(20)
print("Count:", cnt)

# Sorting the list
l.sort()
print("Sorted:", l)

# Reversing a list
l.reverse()
print("Reversed:", l)

# Create a copy of the list
l1 = l.copy()
print("Copy:", l1)

# Cleaing the entire list
l.clear()
print("Clear", l)
