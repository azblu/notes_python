sepA = {'@', '{', '}', '*', '/'}
sepB = {'+', '-', '/', '*'}

print(sepA, sepB)
# Union
print(sepA | sepB)
print(sepA.union(sepB))


# Intersecction
print(sepA & sepB)
print(sepA.intersection(sepB))

# Diference
print(sepA - sepB)
print(sepA.difference(sepB))
# symmetric difference
print(sepA ^ sepB)
print(sepA.symmetric_difference(sepB))

res = {x for x in sepA if x not in sepB }
print(res)

# Operators
# Add
sepA.add('$')
print(sepA)

#update
sepA.update({'8', '?'}) 
print(sepA)

#Remove
sepA.remove('{') 
print(sepA)
sepA.discard('}')
print(sepA)

# Clear
sepA.clear()
print(sepA)
