number = 15 # Initialize the variable
while number >=5: # Complete the while loop condition
    print(number, end=" ")
    number -=1 # Increment the variable

# Should print 15 10 5 

def factorial(n):
    result = n
    start = n
    n -= 1
    while n>0: # The while loop should execute as long as n is greater than 0
        result *= n # Multiply the current result by the current value of n
        n = n-1 # Decrement the appropriate variable by -1
    return result


print(factorial(3)) # Should print 6
print(factorial(9)) # Should print 362880
print(factorial(1)) # Should print 1