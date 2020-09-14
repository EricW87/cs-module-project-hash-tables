# Your code here
import random
import math
lookup_table = []

def slowfun_too_slow(x, y):
    v = math.pow(x, y)
    v = math.factorial(v)
    v //= (x + y)
    v %= 982451653

    return v

def slowfun(x, y):
    """
    Rewrite slowfun_too_slow() in here so that the program produces the same
    output, but completes quickly instead of taking ages to run.
    """
    # Your code here
    if len(lookup_table) == 0: #runs only if lookup_table is empty
        for i in range(2, 14): #possible values of x
            for j in range(3, 6): #possible values of y
                lookup_table.append(slowfun_too_slow(i,j)) #calculates value for x & y

    return lookup_table[3*(x - 2) + (y - 3)]

                
# Do not modify below this line!

for i in range(50000):
    x = random.randrange(2, 14)
    y = random.randrange(3, 6)
    print(f'{i}: {x},{y}: {slowfun(x, y)}')
