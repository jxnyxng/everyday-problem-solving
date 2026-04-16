# 백준 1262번

N, r1, c1, r2, c2 = map(int, input().split())
D = 2 * N - 1

for i in range(r1, r2 + 1):
    for j in range(c1, c2 + 1):
        i %= D
        j %= D
        
        dis = abs(N - 1 - i) + abs(N - 1 - j)
        
        if dis > N-1:
            print(".", end="")
        else:
            print(chr(ord('a') + dis % 26), end='')

    print()