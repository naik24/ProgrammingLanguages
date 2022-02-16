"""
USING LISTS AS STACKS

The list methods make it very easy to use a list as a stack,
where the last element added is the first element retrieved
("last-in, first-out"). To add an item to the top of the
stack, use append(). To retrieve an item from the top of the
stack, use pop() without an explicit index.

reference:
https://docs.python.org/3/tutorial/datastructures.html/5.1.1
"""


# The list 'versions' is a list of version rolled out by a software version
versions = ['v1.0', 'v1.1', 'v1.2', 'v2.0']

# They just made a new software version v2.1 and are rolling it out
print("Rolling out new version....\n")
versions.append('v2.1') 
print("The current version is:", versions[-1])

# But for some reason this version doesnt seem to work properly. So they
# decide to roll back to previous version until they find a fix for v2.1
print("\nError found in the current version")
print("\nRolling back to previous versions...")
versions.pop() 

# Therefore, the current version of the software is:
print("\nThe current version is:", versions[-1])



