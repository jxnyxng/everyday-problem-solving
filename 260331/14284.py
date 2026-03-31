# 백준 14284번

# s->t 가중치가 최소이면 됨
# d_table[t]
# 간선 다 연결시켜놓고 최소 찾는거랑 같은 말?
import heapq

n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

s, t = map(int, input().split())    

def dijkstra(st):
    d_table = [float('inf')] * (n+1)
    d_table[st] = 0
    pq = []
    # now node, now dist
    heapq.heappush(pq, (st, 0))
    
    while pq:
        now_node, now_dist = heapq.heappop(pq)
        
        for next_node, next_dist in graph[now_node]:
            new_dist = now_dist + next_dist
            
            if new_dist > d_table[next_node]:
                continue
                
            d_table[next_node] = new_dist
            heapq.heappush(pq, (next_node, new_dist))

    return d_table            

ans_table = dijkstra(s)
print(ans_table[t])