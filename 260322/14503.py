# 백준 14503번

N, M = map(int, input().split())
r, c, d = map(int, input().split())
ground = [list(map(int, input().split())) for _ in range(N)]

dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]
ans = 0

while True:
    # 1. 현재 위치 청소
    if ground[r][c] == 0:
        ground[r][c] = 2 
        ans += 1
    
    # 2. 주변 4칸 확인
    fin = True
    for _ in range(4):
        d = (d + 3) % 4
        nr = r + dr[d]
        nc = c + dc[d]
        
        # 앞쪽 칸이 청소되지 않은 빈 칸이면 전진
        if ground[nr][nc] == 0:
            r, c = nr, nc
            fin = False
            break
            
    # 3. 네 방향 모두 청소되었거나 벽
    if fin:
        back_d = (d + 2) % 4
        br = r + dr[back_d]
        bc = c + dc[back_d]
        
        if ground[br][bc] == 1:
            break
        else:
            r, c = br, bc

print(ans)