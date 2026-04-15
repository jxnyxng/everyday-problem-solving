# 백준 5397번

T = int(input())

for _ in range(T):
    L = []
    R = []
    data = input()

    for i in data:
        if i == '-':
            if L:
                L.pop()
        elif i == '<':
            if L:
                R.append(L.pop())
        elif i == '>':
            if R:
                L.append(R.pop())
        else:
            L.append(i)
            
    L.extend(reversed(R))
    print(''.join(L))