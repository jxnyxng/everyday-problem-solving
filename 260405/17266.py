# 백준 17266번

n = int(input())
m = int(input())
l = list(map(int, input().split()))
ans = l[0]

for i in range(1, m):
    ans = max(ans, (l[i]-l[i-1]+1) // 2)

ans = max(ans, n - l[-1])
print(ans)
