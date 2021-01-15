# Write a program that computes the value of a+aa+aaa+aaaa with a given d9igit as the value of a.


val = input()
for i in range(1, val + 1):
    sum = int(0)
    sum = sum + int(pow(9, i))
print(sum)
