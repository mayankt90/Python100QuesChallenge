# Use a list comprehension to square each odd number in a list. The list is input by a sequence of comma-separated numbers. >Suppose the following input is supplied to the program:

# 1,2,3,4,5,6,7,8,9


l = input().split(",")
total = []
for i in l:
    i = int(i)
    if i % 2 == 0:
        continue
    else:
        total.append(str(i * i))
print(",".join(total))
