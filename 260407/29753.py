# 백준 29753번

N, X = input().split()
N = int(N)
X = int(round(float(X) * 100))

d = {
    "F" : 0, "D0" : 100, "D+" : 150, "C0" : 200, "C+" : 250, 
    "B0" : 300, "B+" : 350, "A0" : 400, "A+" : 450
}

cng = 0
total_credit = 0

for i in range(N-1):
    credit, grade = input().split()
    credit = int(credit)
    total_credit += credit
    cng += (credit * d[grade])

next_credit = int(input())
total_credit += next_credit
ans = 'impossible'

for g in d:
    new_cng = (d[g] * next_credit)
    total_score = cng + new_cng
    gpa = total_score // total_credit

    if gpa > X:
        ans = g
        break

print(ans)        
