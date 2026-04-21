# 백준 16500번

s = input()
n = int(input())
a = [input() for i in range(n)]
dp = [False for _ in range(len(s) + 1)]
dp[0] = True

for i in range(len(s)):
    if not dp[i]: continue

    for t in a:
        if s[i:i + len(t)] == t:
            dp[i + len(t)] = True
            
print(int(dp[len(s)]))