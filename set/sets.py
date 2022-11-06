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
