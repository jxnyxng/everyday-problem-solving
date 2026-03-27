# 백준 5598번

l = list(input())

for i in range(len(l)):
    k = ord(l[i]) - 3
    
    if k < ord('A'):
        k += 26
    l[i] = chr(k)
    
print(''.join(l))