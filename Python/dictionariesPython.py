"""
Unlike sequences, which are indexed by a range of numbers, dictionaries
are indexed by keys, which can be immutable type; strings and numbers can
always be keys

referenece:
5.5 Dictionaries [https://docs.python.org/3/tutorial/datastructures.html#using-lists-as-queues]
"""

#simple dict
employee = {52991: 'Patrick', 52891: 'Lily', 56879: 'Alex'}

for empid in employee:
    print(empid, employee[empid])

# Performing list(d) on a dict returns a list of keys
print('\n', list(employee))

# The dict() constructor
f1= dict([('Mercedes','Hamilton'), ('RedBull','Max'), ('Aston Martin','Vettel')])
print(f1)

## Looping Techniques

# Using items() method
for k, v in f1.items():
    print(k, v)



