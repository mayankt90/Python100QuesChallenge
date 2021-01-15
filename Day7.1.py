# Define a class with a generator which can iterate the numbers, which are divisible by 7, between a given range 0 and n.


class first_cls:
    def div_seven(self, n):
        n = int(n)
        lst = []
        for i in range(0, n + 1):
            if int(i) % 7 == 0:
                lst.append(str(i))
        return lst


s = input("Enter the number: ")
l = first_cls().div_seven(s)
for i in l:
    print(i)
