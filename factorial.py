# You will have to figure out what parameters to include
# 🚨 All functions must use recursion 🚨

# This function returns the factorial of a given number.

def factorial(n, result = 1):
    # Write code here
    result *= n
    n -= 1
    if n == 1:
        return result
    return factorial(n, result)
print(factorial(5))