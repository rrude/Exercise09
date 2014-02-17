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



# Finds the item i in the list l.... RECURSIVELY
def find(l, i):
    if l[0] == i:
        return True
    else:
        return find(l[1:], i)



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
    if folds == 0:
        return width, height   
#next line checks if user entered width and height incorrectly, ensures paper always folded lengthwise        
    elif width >= height:
        return fold_paper( height / 2, width, folds - 1 )
    else:
        return fold_paper( width / 2, height, folds - 1 )    
    


# Count up
# Print all the numbers from 0 to target 
# we need to use a list to append items from recursion, but the function requires a single int
# this solution assumes that n will represent 0, in order to count up from 0 
def count_up(target, n):
    #this is our base case we are increasing n by 1 until it is equal to target
    if n == target:
        return [target]
        #I'm returning target because this will complete the count since range is exclusive
    else:
        #here I'm creating a list so I can reference the first item, which will change with each loop
        listy = range(n, target)
        # I'm assigning the fist value in the range to x our range gets smaller each time because the starting 
        #point of n increases each time getting closer to target
        x = listy[0]
        # need to return x as a list so that it can be appended rather than calculating a sum
        return [x] + count_up(target, n + 1)
#zero was specified in question five is a random choice for target
print count_up(5, 0)            



