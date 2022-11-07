fullname = lambda x, y : f'{x} {y}'
print(fullname('Sam', 'Johnson'))


names = ['Sam', 'Paula', 'Valentina', 'Justin']
lastnames = ['Smith', 'Johnson', 'Williams', 'Brown']
print(list(map(lambda x, y : f'{x} {y}', names, lastnames)))


suma = lambda x, y: x+y
resta = lambda x, y: x-y
suma_resta = lambda x, y, z, p: suma(x, y) + resta(z, p)
print(suma_resta(4,6,8,2))

a = [1, 5, 8]
b = [7, 9 , 2, 3]
print(list(map(lambda x, y: x+y, a, b)))
