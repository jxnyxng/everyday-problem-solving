# 백준 1043번

N, M = map(int, input().split())
know_truth = list(map(int, input().split()))

if know_truth[0] == 0:
    print(M)
    exit()

truth_set = set(know_truth[1:])
parties = []

for _ in range(M):
    party = list(map(int, input().split()))
    parties.append(set(party[1:]))

for _ in range(M):
    for party in parties:
        if party & truth_set: 
            truth_set.update(party) 

ans = 0
for party in parties:
    if not (party & truth_set): 
        ans += 1

print(ans)