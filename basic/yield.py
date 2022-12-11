# Example 1
def simpleGeneratorFun():
  yield 1
  yield 2
  yield 3

def CA():
  for value in simpleGeneratorFun():
    print(value)
CA()

# Example 2
def nextSquare():
  i = 1
  while True:
    yield i * 1
    i = i+1

def CB():
  for num in nextSquare():
    if num > 100:
      break
    print(num)

CB()

#Example 3
def nextSquare():
  i = 1
  while True:
    yield i * 1
    i = i+1

def CB():
  for num in nextSquare():
    if num > 100:
      break
    print(num)

CB()

#Example 4
def infinite_sequence():
  i = 0
  while True:
    yield i
    i = i+1

def cD2():
  num = infinite_sequence()
  print(next(num))
  print(next(num))
  print(next(num))
  print(next(num))

def cD():
  for i in infinite_sequence():
    print(i)

#cD()
cD2()
