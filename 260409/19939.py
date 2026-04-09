# 백준 19939번

n, k = map(int, input().split())
c = k*(k+1)//2
print(-1 if n<c else k-1 if (n - c) % k == 0 else k)    