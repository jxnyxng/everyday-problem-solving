# 백준 1106번

c, n = map(int, input().split())
data = []

for _ in range(n):
    v, p = map(int, input().split())
    data.append((v, p))

limit = c + 100
dp = [float('inf')] * (limit + 1)
dp[0] = 0

for cost, customer in data:
    for i in range(customer, limit + 1):
        if dp[i - customer] != float('inf'):
            dp[i] = min(dp[i], dp[i - customer] + cost)

print(min(dp[c:]))