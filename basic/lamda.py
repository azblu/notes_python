fullname = lambda x, y: f'{x} {y}'
print(fullname('Violeta', 'Justin'))

# Map
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

# Filter
numbers = list(range(0,15))
new_numbers = list(filter(lambda x: x%2==0, numbers))
print(new_numbers)


matches = [
  {
    'home_team': 'Bolivia',
    'away_team': 'Uruguay',
    'home_team_score': 3,
    'away_team_score': 1,
    'home_team_result': 'Win'
  },
  {
    'home_team': 'Brazil',
    'away_team': 'Mexico',
    'home_team_score': 1,
    'away_team_score': 1,
    'home_team_result': 'Draw'
  },
  {
    'home_team': 'Ecuador',
    'away_team': 'Venezuela',
    'home_team_score': 5,
    'away_team_score': 0,
    'home_team_result': 'Win'
  },
]

new_list = list(filter(lambda x: x['home_team_result'] =='Win', matches))
print(new_list)


# Reduce

import functools

numbers = [1, 2, 3, 4]

result = functools.reduce(lambda counter, item: counter + item, numbers )

print(result)


def accum(counter, item):
  print('counter => ',counter)
  print('item => ',item)
  return counter + item

result = functools.reduce(accum, numbers)

print(result)

