# 백준 10253번

from fractions import Fraction

for i in range(int(input())):
    a,b=map(int,input().split())
    
    while(a!=1):
        c=b//a+1
        a=a*c-b
        b=b*c
        a,b=map(int,str(Fraction(a,b)).split('/'))
    print(b)


