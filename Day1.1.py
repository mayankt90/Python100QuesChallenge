# Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5, between 2000 and 3200 (both included).The numbers obtained should be printed in a comma-separated sequence on a single line.


list = []
for i in range(2000, 3201):
    if i % 7 == 0 and i % 5 != 0:
        list.append(str(i))
print(",".join(list))


# Join is a string function which has two place -1.join(-2) 2 is an iterable and 1 is the thing that has to be joined to the iterable.