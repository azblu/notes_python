sepA = {'@', '{', '}', '*', '/'}
sepB = {'+', '-', '/', '*'}

print(sepA, sepB)
# Union
print(sepA | sepB)
# Intersecction
print(sepA & sepB)
# Diference
print(sepA - sepB)
# the elements are both set
print(sepA ^ sepB)

res = {x for x in sepA if x not in sepB }
print(res)
