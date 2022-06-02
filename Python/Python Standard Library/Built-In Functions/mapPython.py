def square(num):
    return num**2

numbers = [x for x in range(10)]

mapped = map(square, numbers)
print(list(mapped))
