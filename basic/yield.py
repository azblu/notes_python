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
