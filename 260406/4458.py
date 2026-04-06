# 백준 4458번

n = int(input())
for i in range(n):
    inp = list(input())
    inp[0] = inp[0].upper()

    print(''.join(inp))
