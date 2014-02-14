l = [1, 3, 2, 9, 17]

# Multiply all the elements in a list
def multiply_list(l):
    if len(l) == 1:
        return l[0]
    else:
        return l[0] * multiply_list(l[1:])

# Return the factorial of n
def factorial(n):
    total = 1
    if n == 1:
        return 1
    else:
        total = factorial(n-1) * n
    return total    

# Count the number of elements in the list l
def count_list(l):
    if len(l) == 1:
        return 1
    else:
        return 1 + count_list(l[1:])

# Sum all of the elements in a list
def sum_list(l):
    if len(l) == 1:
        return l[0]
    else:    
        return l[0] + sum_list(l[1:])

# Reverse a list without slicing or loops
def reverse(l):
    if len(l) == 1:
        return l
    else:
        x = l.pop()
        return [x] + reverse(l)

# Fibonacci returns the nth fibonacci number. The nth fibonacci number is
# defined as fib(n) = fib(n-1) + fib(n-2)
def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

print fibonacci(4)

# Finds the item i in the list l.... RECURSIVELY
def find(l, i):
    if l[0] == i:
        return True
    else:
        return find(l[1:], i)

print find(l, 2)

# Determines if a string is a palindrome
def palindrome(some_string):
    #compare first item with last if true run function again if false return false
    if len(some_string) <= 1:
        return True
    elif some_string[0] != some_string[-1]:
        return False
    else:
        new_string = some_string[1:-1]
        return palindrome(new_string)    

    

# Given the width and height of a sheet of paper, and the number of times to fold it, return the final dimensions of the sheet as a tuple. Assume that you always fold in half along the longest edge of the sheet.
def fold_paper(width, height, folds):
    return (0, 0)

# Count up
# Print all the numbers from 0 to target
def count_up(target, n):
    return