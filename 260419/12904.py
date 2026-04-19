# 백준 12904번

s = list(input())
t = list(input())
c = False

while t:
    if t[-1] == 'A':
        t.pop()
    elif t[-1] == 'B':
        t.pop()
        t.reverse()

    if s == t:
        c = True
        break

print(1 if c else 0)