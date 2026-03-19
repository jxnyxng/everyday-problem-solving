# 백준 10162번

# 300초 60초 10초 버튼
# 일의 자리가 0이 아니면 -1

T = int(input())

if T % 10 != 0:
    print(-1)
else:
    print((T//300), (T%300)//60, ((T%300)%60)//10)    
    

# if T % 10 != 0:
#     print(-1)
#     exit()
    
# A_cnt, B_cnt, C_cnt = 0, 0, 0
# new_T = T

# if new_T >= 300:
#     A_cnt = new_T//300
#     new_T = new_T % 300

# if new_T >= 60:
#     B_cnt = new_T//60
#     new_T = new_T % 60

# if new_T >= 10:
#     C_cnt = new_T // 10
#     new_T = new_T % 10

# print(A_cnt, B_cnt, C_cnt)    