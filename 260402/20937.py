# 백준 20937번
n = int(input())
l = list(map(int, input().split()))
d = {}
for i in l: d[i] = d.get(i, 0) + 1
print(max(d.values()))    