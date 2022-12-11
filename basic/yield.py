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
