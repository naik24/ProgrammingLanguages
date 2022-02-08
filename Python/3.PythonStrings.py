# String input from user
name = input("What is your name? ")
age = input("How old are you? ")

# Using escape characters
print("New Profile...\n")
print("ID\tName\tAge\n")
print('01\t'+name+"\t"+age+"\n")

# To avoid interpretation of '\' as a special character, we use raw strings
print(r'Location of new profile is C:\newprofile\id01')

# You can break long strings into smaller ones in Python
print('\nPrasad Naik is an aspring '
      'Computer Vision researcher from India.')

# Indexing of Strings
for i in range(len(name)):
    print(name[i])
    



