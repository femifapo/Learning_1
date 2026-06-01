# Create a function to calculate the factorial of a number
def factorial(n):
    if n < 0:
        return "Factorial is not defined for negative numbers"
    elif n == 0 or n == 1:
        return 1
    else:
        result = 1
        for i in range(2, n + 1):
            result *= i
        return result
    

# Test the functionprint(factorial(5))  # Output: 120
print(factorial(0))  # Output: 1
print(factorial(-3))  
print(factorial(5))  # Output: 120  