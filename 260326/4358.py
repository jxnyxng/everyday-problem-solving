# 백준 4358번
import sys

dic = {}
trees = 0

for text in sys.stdin:
    text = text.rstrip()
    
    if not text: 
        continue
        
    if text in dic:
        dic[text] += 1
    else:
        dic[text] = 1
    trees += 1

sorted_trees = sorted(dic.keys())
for tree in sorted_trees:
    print("%s %.4f" % (tree, (dic[tree] / trees) * 100))
