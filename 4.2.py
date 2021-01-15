# Write a program that computes the value of a+aa+aaa+aaaa with a given digit as the value of a.

# upto the variable
val = input()
for i in val:
    # i = int(i)
    sum = 0
    temp = 0
    temp += pow(9, int(i))
    sum += temp
print(sum)

# For this question only 4 digits
a = input()
total, tmp = 0, str()
for i in range(4):
    tmp += a
    total += int(tmp)
print(total)