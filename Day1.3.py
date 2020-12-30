# With a given integral number n, write a program to generate a dictionary that contains (i, i x i) such that is an integral number between 1 and n (both included). and then the program should print the dictionary.Suppose the following input is supplied to the program: 8

l = int(input("Enter the number: "))
dic = {}
for i in range(l):
    dic[i + 1] = (i + 1) * (i + 1)
print(dic)


# using dict comprehension
# n = int(input())
# ans={i : i*i for i in range(1,n+1)}
# print(ans)
