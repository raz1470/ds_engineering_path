
# Function to tests
def calculate_mean(numbers):
    return sum(numbers) / len(numbers)

# Tests
def test_calculate_mean():
    # Test case 1: Basic test with positive numbers
    assert calculate_mean([1, 2, 3, 4, 5]) == 3.0

    # Test case 2: Test with a single number
    assert calculate_mean([10]) == 10.0

    # Test case 3: Test with a mix of positive and negative numbers
    assert calculate_mean([-2, 0, 2]) == 0.0
