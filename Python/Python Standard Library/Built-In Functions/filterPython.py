numbers = [x for x in range(0, 20)]

def oddnum(number):
    if number % 2 != 0:
        return number

oddnums = list(filter(oddnum, numbers))

print(oddnums)
