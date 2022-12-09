def suma(x,y):
  return x+y

def resta(x, y):
  return x-y

def operation(x,y,func):
  return func(x,y)

print(operation(2,5, suma))
print(operation(2,5, resta))
