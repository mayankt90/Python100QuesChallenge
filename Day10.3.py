# Define a function which can generate and print a tuple where the value are square of numbers between 1 and 20 (both included).


def printTuple():
    l = []
    for i in range(1,21):
        l.append(i**2)
    print(tuple(l))
printTuple()