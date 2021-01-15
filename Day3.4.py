# Write a program that accepts a sentence and calculate the number of letters and digits.


l = input()
letter, digit = 0, 0
for i in l:
    if ("a" <= i and i <= "z") or ("A" <= i and "Z"):
        letter += 1
    if "0" <= i and i <= "9":
        digit += 1
print("LETTERS ",letter)
print("DIGITS ",digit)
