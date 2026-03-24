# 백준 1707번

# 인접한 노드는 다른 색으로 칠하기
# 이미 칠해져있는 색과 다른 색을 칠해야 하면
# 종료 하고 NO
import sys

sys.setrecursionlimit(20000)

K = int(input())

def dfs(start, group):
    global error
    
    if error:
        return
    
    visited[start] = group
    
    for next_node in graph[start]:
        # 이미 방문한 다음 노드이면
        if not visited[next_node]:
            dfs(next_node, -group)
        elif visited[next_node] == visited[start]:
            error = True
            return
            

for _ in range(K):
    V, E = map(int, input().split())
    visited = [False] * (V + 1)
    graph = [[] for _ in range(V + 1)]
    error = False
    
    for _ in range(E):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)
    
    for i in range(1, V + 1):
        if not visited[i]:
            dfs(i, 1)
            if error:
                break
    
    if error:
        print('NO')
    else:
        print('YES')

