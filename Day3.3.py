# Write a program, which will find all such numbers between 1000 and 3000 (both included) such that each digit of the number is an even number.The numbers obtained should be printed in a comma-separated sequence on a single line.


l = []
for i in range(1000, 3001):

    if i % 2 == 0:
        i = str(i)
        l.append(i)
# l = str(l)
print(",".join(l))
print()


# Every digit Problem:
ls = []
for i in range(1000,3001):
    i = str(i)
    if (int(i[0])%2 == 0) and (int(i[1])%2 == 0) and (int(i[2])%2 == 0) and (int(i[3])%2 == 0):
        
        ls.append(i)
print(','.join(ls))


# or


lst = []

for i in range(1000,3001):
    flag = 1
    for j in str(i):          # every integer number i is converted into string
        if ord(j)%2 != 0:     # ord returns ASCII value and j is every digit of i also str can be changed inti int.
            flag = 0          # flag becomes zero if any odd digit found
    if flag == 1:
        lst.append(str(i))    # i is stored in list as string

print(",".join(lst))

