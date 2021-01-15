# Write a program that accepts a sentence and calculate the number of upper case letters and lower case letters.

s = input()
upr = 0
lwr = 0
for i in s:
    if "a" <= i <= "z":
        lwr += 1
    elif "A" <= i <= "z":
        upr += 1
print("UPPER CASE ",upr)
print("LOWER CASE ",lwr)
