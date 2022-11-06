fruits = list()
fruits = ['Banana', 'Cherry', 'Avocado']
print(fruits)

# Add
fruits.append('Pineapple')
print(fruits)

# Pop
fruits.pop()
print(fruits)

# Sort
fruits.sort()
print(fruits)

# Insert
fruits.insert(2, 'Coco')
print(fruits)

# List Comprehension
print('Create List Comprehension')
sqare = list(map(lambda x: x**2, range(10)))
print(sqare)

print([(x, y) for x in [1,2,3] for y in [3, 1, 4] if x!=y])

animals = ['cat', 'doc', 'bird', 'doc', 'duck', 'rabbit', 'hamster', 'snake', 'doc']

# Count
print(animals.count('doc'))

# Index
print(animals.index('snake'))

# Reverse
animals.reverse()
print(animals)








