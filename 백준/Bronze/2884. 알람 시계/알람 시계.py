H, M = map(int,input().split())

if H != 0:
    time = H * 60 + M
    ans = time - 45
    ans_H = ans // 60
    ans_M = ans % 60

else:
    time = (H+24) * 60 + M
    ans = time - 45
    ans_H = ans // 60
    ans_M = ans % 60
if ans_H == 24:
    ans_H = 0
print(ans_H, ans_M)