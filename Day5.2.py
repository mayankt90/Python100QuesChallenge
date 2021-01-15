# Write a program that computes the net amount of a bank account based a transaction log from console input. The transaction log format is shown as following:

# D 100
# W 200
# D means deposit while W means withdrawal.

total = 0
i = 0
while True:
    s = input().split()
    if not s:
        break
    # cm, num = map(str, s)

    if s[i] == "D":
        total += int(s[i + 1])
        # i = i+1
    if s[i] == "W":
        total -= int(s[i + 1])

    # i = i+1

print(total)
# Or


# lst
