# 백준 23970번

N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

def sol(a, b):
    for i in range(N - 1, 0, -1):
        for j in range(i):
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]
                if a[j+1] == b[j+1] and a == b:
                    print(1)
                    exit()
    print(0)

if A == B:
    print(1)
    exit()
else:
    sol(A, B)