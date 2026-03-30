import itertools
n = int(input())
k = int(input())
print(len(set("".join(i) for i in itertools.permutations([input().strip() for _ in range(n)], k))))