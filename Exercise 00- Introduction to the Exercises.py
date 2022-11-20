#Intermediate
# you can define your own functions
def greet(name):
    print("Welcome to " + name + "!")

# go ahead and enter your own name in variable 'name' below to get a warm welcome from us.

def main():
    name = "Building AI"
    greet(name)

main()


#Advanced

# Solving this exercise will be helpful in the first actual exercise
# (Exercise 1), so consider using this as an opportunity to warm up. 
#
# Your task is the define a function that returns the so called 
# factorial: for any non-negative integer n, the factorial is defined
# as 1 * 2 * ... * n. For example, factorial(5) = 1*2*3*4*5 = 120.
#
# Hint: the simplest way to compute the factorial is to use a
# recursive function, or in other words, a function that calls 
# itself as in 
#     factorial(n) = n * factorial(n-1)
# The recursion should terminate at factorial(0) = 1 so that we
# don't create an infinite loop.
def factorial(n): 
    if n == 0: 
        return 1
    else: 
        return n * factorial(n-1)  # <-- replace this with the recursive call
        
print(factorial(6))              # this should print 720