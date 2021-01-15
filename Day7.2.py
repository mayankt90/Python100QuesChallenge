import math

x, y = 0, 0
while True:
    s = input().split()
    if not s:
        break
    if s[0] == "up":
        x += s[1]
    if s[0] == "down":
        x -= s[1]
    if s[0] == "left":
        y += s[1]
    if s[0] == "right":
        y -= s[1]

dist = round(math.sqrt(x ** 2 + y ** 2))
print(dist)