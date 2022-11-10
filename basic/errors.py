suma = lambda x, y: x + y
assert suma(2, 2) == 4

age = 10
if age<18:
  raise Exception('No se permiten menores de edad')
  
  
  
try:
except Exception as e:
raise
else:
pass:
finally:
pass

try:
  print(5/0)
except ZeroDivisionError as error:
  print(error)
