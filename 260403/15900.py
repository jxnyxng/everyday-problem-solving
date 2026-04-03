# 백준 15900번

import sys
from collections import deque
input = sys.stdin.readline

MAX = float('inf')
n = int(input())

edges = [[] for _ in range(n + 1)]

for _ in range(n - 1):
    a, b = map(int, input().split())

    edges[a].append(b)
    edges[b].append(a)

q = deque()
q.append(1)

dist = [MAX] * (n + 1)
dist[1] = 0
s = 0

while q:
    now_node = q.popleft()
    
    for next_node in edges[now_node]:
        if dist[next_node] > dist[now_node] + 1:
            q.append(next_node)
            dist[next_node] = dist[now_node] + 1
        
    if len(edges[now_node]) == 1 and now_node != 1:
        s += dist[now_node]

print("Yes" if s % 2 == 1 else "No")