# Write a program that accepts a sequence of whitespace separated words as input and prints the words after removing all duplicate words and sorting them alphanumerically.

# Suppose the following input is supplied to the program:

# hello world and practice makes perfect and hello world again
# Then, the output should be:

# again and hello makes perfect practice world


l = input().split(" ")
print(" ".join(sorted(list(set(l)))))


# method 2
word = input().split()

for i in word:
    if (
        word.count(i) > 1
    ):  # count function returns total repeatation of an element that is send as argument
        word.remove(i)  # removes exactly one element per call

word.sort()
print(" ".join(word))