# 백준 1520번

import sys
sys.setrecursionlimit(10**5)

M, N = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(M)]
dp = [[-1] * N for _ in range(M)]

dxs = [-1, 1, 0, 0]
dys = [0, 0, -1, 1]

def in_range(x, y):
    return 0 <= x < M and 0 <= y < N

def dfs(x, y):
    if x == M - 1 and y == N - 1: return 1
    
    if dp[x][y] != -1: return dp[x][y]
    
    dp[x][y] = 0
    
    for i in range(4):
        nx = x + dxs[i]
        ny = y + dys[i]
        
        if in_range(nx, ny) and grid[nx][ny] < grid[x][y]:
                dp[x][y] += dfs(nx, ny)
                
    return dp[x][y]

print(dfs(0, 0))