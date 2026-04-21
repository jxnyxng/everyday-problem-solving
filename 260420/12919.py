# 백준 12919번

S = list(input())
T = list(input())

def dfs(text):
    if text == S:
        print(1)
        exit()

    if len(text) == 0: 
        return

    if text[-1] == 'A': 
        dfs(text[:-1])

    if text[0] == 'B': 
        dfs(text[1:][::-1])

    return 0

print(dfs(T))