# 백준 2578번
arr = []
ans_g = []
for i in range(5):
    arr.append(list(map(int, input().split())))

for _ in range(5):
    ans_g.extend(list(map(int, input().split())))

cnt = 0
Bingo = 0

# 빙고 됐는지 찾는 함수
def check():
    rechck = 0
    # 가로 세로
    for i in range(5):
        row_chck = 0
        col_chck = 0
        
        for j in range(5):
            if arr[i][j] == 0:
                row_chck += 1
            
            if arr[j][i] == 0:
                col_chck += 1      
                
        if row_chck == 5:
            rechck += 1

        if col_chck == 5:
            rechck += 1    
                           
    # 대각선
    l_chck = 0
    r_chck = 0
    for i in range(5):
        if arr[i][i] == 0:
            l_chck += 1

        if arr[i][4-i] == 0:
            r_chck += 1    
            
    if l_chck == 5:
        rechck += 1
        
    if r_chck == 5:
        rechck += 1
        
    if rechck >= 3:
        return True
    else:
        return False

# 부른 번호를 내 빙고 칸에서 찾기    
def finding(a):
    for i in range(5):
        for j in range(5):
            if arr[i][j] == a:
                arr[i][j] = 0
                return

# 순서대로 번호를 부른다                
def get_ans():
    global cnt
    for a in ans_g:
        cnt += 1
        finding(a)
    
        if check():
            return cnt
    return -1

res = get_ans()
print(res)
