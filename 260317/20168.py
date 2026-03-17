# 백준 20168번
import heapq

N, M, A, B, C = map(int, input().split())
graph = [[] for _ in range(N+1)]

for _ in range(M):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

def dijkstra(st, en, total_money):
    q = [(0, st, total_money)]
    best_money = [-1] * (N + 1)

    while q:
        max_paid, curr_node, curr_money = heapq.heappop(q)

        # 목적지 도착하면 바로 리턴 (우선순위 큐니까 이게 무조건 최소 요금)
        if curr_node == en:
            return max_paid

        if best_money[curr_node] >= curr_money:
            continue

        best_money[curr_node] = curr_money

        for next_node, next_pay in graph[curr_node]:
            new_money = curr_money - next_pay
            
            if new_money < 0:
                continue
            
            new_paid = max(max_paid, next_pay)
            heapq.heappush(q, (new_paid, next_node, new_money))

    return -1

print(dijkstra(A, B, C))