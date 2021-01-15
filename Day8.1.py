# Write a program to compute the frequency of the words from the input. The output should output after sorting the key alphanumerically.


ss = input().split()
dict = {}
for i in ss:
    dict.setdefault(i, ss.count(i))
dict = sorted(dict.items())

for i in dict:
    print(i[0], i[1])
