# Initialization
tup = tuple()
colors = ('Blue', 'Red', 'Green')
numbers = (1, 8, 3, 4, 6, 9, 2, 5, 7, 0)

# Slices
print(colors[0])
print(colors[-1])
print(numbers[:])
print(numbers[3:])
print(numbers[3::2])


print(*colors)


vocales = ['a', 'e', 'i', 'o']
numbers = [1, 2, 3]
new_tuple = (vocales, numbers)
print(new_tuple)
new_tuple[0].append('u')
print(new_tuple)
