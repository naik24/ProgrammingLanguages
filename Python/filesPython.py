# simple file
f = open('SimpleFile' , 'w')

"""
File modes:
w : writing
r: reading
a: appending
r+: both reading and writing
'b': binary mode
"""

# It is good practive to use the 'with' keyword when dealing with file objects.
# The advantage is that the file is properly closed after its suite finishes, even
# iff an exception is raised at some point. Using 'with' is also much shorter than
# writing equivalent try-finallly blocks
with open('SimpleFile', "w") as f:
    f.write('First Line\n Second Line')
    
"""
WARNING: Calling f.write() without using the 'with' keyword of calling f.close()
might result in the arguments of f.write() not being completely written to disk,
even if program exits successfully
"""

# file.readline()
g = open('Newfile', "w")
g.write('Hello\n')
g.write('Good Morning')
g.close()

with open("Newfile", "r") as g:
    for line in g:
        print(line)
    print(g.tell())

# saving structured data with json
import json
"""
When you want to save complex data types like nested lists and dictionaries,
parsing and serializing by hand becomes complicated. Python allows us to use
JSON. The standard module json can take Python data hierarhchies, and convert
them to string representations; this process is called serializing.

Reconstructing the data from the string representation is called deserializing.
"""

info = [52991, 'Peter', 'Accounts']
with open('SimpleFile', "r+") as f:
    json.dump(info, f)

with open('SimpleFile', "r") as f:
    l = json.load(f)

print(l)
