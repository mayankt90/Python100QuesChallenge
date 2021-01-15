# Write a program that calculates and prints the value according to the given formula:

# Q = Square root of [(2 _ C _ D)/H]

# Following are the fixed values of C and H:

# C is 50. H is 30.

from math import sqrt

p = 0
l = list(map(int, input().split(",")))
for i in l:
    q = (100 * i) / 30
    q = sqrt(q)
    q = int(q)
    l[p] = q
    p = p + 1
l = [str(i) for i in l]

print(",".join(l))


# from math import sqrt # import specific functions as importing all using *
# is bad practice

C, H = 50, 30


def calc(D):
    return sqrt((2 * C * D) / H)


D = [int(i) for i in input().split(",")]  # splits in comma position and set up in list
D = [int(i) for i in D]  # converts string to integer
D = [calc(i) for i in D]  # returns floating value by calc method for every item in D
D = [round(i) for i in D]  # All the floating values are rounded
D = [
    str(i) for i in D
]  # All the integers are converted to string to be able to apply join operation

print(",".join(D))