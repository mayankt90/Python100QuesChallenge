# Define a function which can generate a list where the values are square of numbers between 1 and 20 (both included). Then the function needs to print the last 5 elements in the list.

# Method 1
def printList():
    l = [i ** 2 for i in range(1, 21)]
    for i in range(19, 14, -1):
        print(l[i])


printList()


# Method 2
def printSqr():
    sqrl = [i ** 2 for i in range(1, 21)]
    print(sqrl[-5:])

printSqr()
