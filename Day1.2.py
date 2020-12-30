# Write a program which can compute the factorial of a given numbers.The results should be printed in a comma-separated sequence on a single line.Suppose the following input is supplied to the program: 8 Then, the output should be:40320


l = int(input("Enter the Number:"))


def fac(n):
    if n == 0:
        return 1
    return int(fac(n - 1)) * int(n)


print(fac(l))


# lambda arguments : expression
# x = lambda a : a + 10
# print(x(5))