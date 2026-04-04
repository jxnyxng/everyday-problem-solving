# 백준 16956번

r, c = map(int, input().split())
ground = []

def in_range(i, j):
    return 0 <= i < r and 0 <= j < c

dxs, dys = [1, -1, 0, 0], [0, 0, 1, -1]

for i in range(r):
    ground.append(list(input()))

for i in range(r):
    for j in range(c):
        if ground[i][j] != 'S':
            continue
            
        for k in range(4):
            new_r, new_c = i+dys[k], j+dxs[k]

            if not in_range(new_r, new_c):
                continue
                
            if ground[new_r][new_c] == 'W':
                print(0)
                exit()
            elif ground[new_r][new_c] == '.':
                ground[new_r][new_c] = 'D'
print(1)
for i in range(r):
    print("".join(ground[i]))
    