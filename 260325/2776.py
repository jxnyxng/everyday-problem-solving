# 백준 2776번

t = int(input())

for _ in range(t):
    n = int(input())
    numbers = set(map(int, input().split()))
    m = int(input())
    numbers_2 = list(map(int, input().split()))
    
    for num in numbers_2:
        if num in numbers:
            print(1)
        else:
            print(0)