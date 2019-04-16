# factorial(n), which takes in a non-negative integer n and returns n!, which is the product of
# the integers from 1 to n. (0 != 1 by definition.)
# We suggest that you should write your functions so that they raise nice clean errors instead of
# dying messily when the input is invalid. For example, it would be nice if factorial rejected
# negative inputs right away
# otherwise, you might loop forever. You can signal an error like this:
# raise Exception, "factorial: input must not be negative"
# Error handling doesn't affect your lab grade, but on later problems it might save you some angst
# when you're trying to track down a bug.


def factorial(n):
    if n < 1:
        raise Exception("factorial: input must not be negative")
    fact = 1
    for i in range(1, n+1):
        fact = fact * i
    return fact


res = factorial(-3)
print(res)
