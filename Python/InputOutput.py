# f strings
name = 'Anthony'
prog_lang = 'Python'
print(f'My name is {name} and I user {prog_lang} for coding')
print(f'{name:10} {prog_lang:10}')

# .format()
yes_votes = 42_572_654
no_votes = 43_132_495
percentage = yes_votes / (yes_votes + no_votes)
print('{:-9} YES votes  {:2.1%}'.format(yes_votes, percentage))
print('YES : {0:5} NO: {1:5}'.format(yes_votes, no_votes))
print('{0} {1}'.format(name, prog_lang))

# When you dont need fancy output but just want a quick display
# of some variables for debugging purposes, you can convert any
# value to a string using a repr() or str() function
print(repr(name))
print(str(no_votes))

# Old string formatting
print('Percentage votes: %2.2f' %percentage)





