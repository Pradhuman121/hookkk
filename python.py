# def main():
#     print("Welcome to the demo project!")


# if __name__ == "__main__":
#     main()

# print("Hello World")


# Example of Python code with linting issues
# def calculate_square(num):
#     if num < 0:
#         print("Number must be non-negative"):
#     return num**2


# result = calculate_square(5)


# Example of Python code with linting issues
def fibonacci(n):
    fib = [0,    1]
    for i in range(2, n):
        fib.append(fib[i - 1] + fib[i - 2])
    return fib


print(f"The first 10 Fibonacci numbers are: {fibonacci(10)}")


def sum ( a, b):
    return a + b
