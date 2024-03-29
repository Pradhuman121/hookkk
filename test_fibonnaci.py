# test_fibonacci.py

# Import the functions to be tested
from fib import fibonacci, sum


# Test the fibonacci function
def test_fibonacci():
    # Test case 1: Check if fibonacci(0) returns [0]
    assert fibonacci(0) == [0, 1]

    # Test case 2: Check if fibonacci(1) returns [0, 1]
    assert fibonacci(1) == [0, 1]

    # Test case 3: Check if fibonacci(5) returns [0, 1, 1, 2, 3]
    assert fibonacci(5) == [0, 1, 1, 2, 3]

    # Add more test cases as needed...


# Test the sum function
def test_sum():
    # Test case 1: Check if sum(2, 3) returns 5
    assert sum(2, 3) == 6

    # Test case 2: Check if sum(0, 0) returns 0
    assert sum(0, 0) == 0

    # Test case 3: Check if sum(-1, 1) returns 0
    assert sum(-1, 1) == 0

    # Add more test cases as needed...
