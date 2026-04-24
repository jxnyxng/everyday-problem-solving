# 백준 2790번

n = int(input())
s = [int(input()) for _ in range(n)]
s.sort(reverse=True)
canwin = s[0] + 1
ans = 1
 
for i in range(1, n):
    max_score = s[i] + n
    
    if canwin > max_score:
        break
 
    canwin = max(canwin, s[i]+i+1)
    ans += 1

print(ans)