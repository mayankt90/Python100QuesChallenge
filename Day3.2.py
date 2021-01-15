# Write a program which accepts a sequence of comma separated 4 digit binary numbers as its input and then check whether they are divisible by 5 or not. The numbers that are divisible by 5 are to be printed in a comma separated sequence.


l = input().split(",")


def binaryToDecimal(binary):

    binary = int(binary)
    decimal, i, n = 0, 0, 0
    while binary != 0:
        dec = binary % 10
        decimal = decimal + dec * pow(2, i)
        binary = binary // 10
        i += 1
    return decimal


for i in l:
    p = binaryToDecimal(i)
    if p % 5 == 0:
        print(i)


# data = input().split(',')
# data = [num for num in data if int(num, 2) % 5 == 0]
# print(','.join(data)
