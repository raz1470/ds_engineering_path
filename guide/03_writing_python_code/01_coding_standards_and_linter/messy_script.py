
# Function to tests
def calculate_mean(numbers):
    return sum(numbers) / len(numbers)

# this function name is camel case - this won't be fixed by black
def TestCalculateMean():
    # this is a 2 space indent, with unnecessary white space - these will be fixed by black
  assert calculate_mean([ 1, 2, 3, 4, 5 ]) == 3.0
