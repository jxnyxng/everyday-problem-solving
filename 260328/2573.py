from collections import deque

# 1년동안 인접한 0의 개수만큼 감소 -> 시뮬
# 빙산의 개수가 2개가 되면 종료 -> bfs로 빙산 개수 세기

# 인접해있는 칸 수 확인
# 인접해있는 칸 수 만큼 녹이기
# 빙산 개수 확인

N, M = map(int, input().split())
sea = [list(map(int, input().split())) for _ in range(N)]

dx = [0,0,-1,1]
dy = [1,-1,0,0]

def in_range(nx, ny):
    return 0<= nx < N and 0 <= ny < M

def melt(x,y): # 인접해있는 칸 수 확인하기
    for t in range(4):
        nx = x + dx[t]
        ny = y + dy[t]
        
        if not in_range(nx, ny):
            continue
        if sea[nx][ny]==0:
            around_sea[x][y]+=1

# 빙산 몇 개인지 확인하기
def bfs(i,j):
    global temp
    
    q = deque()
    q.append((i,j))
    temp += 1
    
    while q:
        x,y = q.popleft()
        for t in range(4):
            nx = x + dx[t]
            ny = y + dy[t]
            
            if not in_range(nx, ny):
                continue
                
            if sea[nx][ny]!=0 and visited[nx][ny]==0:
                q.append((nx,ny))
                visited[nx][ny] = temp
                
around_sea = [[0 for _ in range(M)] for _ in range(N)]
year = 0

while True:
    temp = 0
    count = 0
    year += 1
    visited = [[0 for _ in range(M)] for i in range(N)]
    
    for i in range(N):
        for j in range(M):
            if sea[i][j] > 0:
                count += 1
                 # 인접한 칸수 확인
                melt(i,j)
                
    if count == 0:
        print(0)
        break
        
    for i in range(N):
        for j in range(M):
            if sea[i][j] > around_sea[i][j]:
                sea[i][j]-=around_sea[i][j]
                around_sea[i][j] = 0
            else:
                sea[i][j] = 0
                around_sea[i][j] = 0


    for i in range(N):
        for j in range(M):
            if sea[i][j] > 0 and visited[i][j] == 0:
                bfs(i,j)

    if temp >= 2:
        print(year)
        break
    