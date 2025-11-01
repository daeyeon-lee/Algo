A = int(input())
B = int(input())
C = int(input())

ans = A * B * C


cnt = {}
for i in range(len(str(ans))):
    cnt[str(ans)[i]] = cnt.get(str(ans)[i],0) + 1


for num in range(10):
    print(cnt.get(str(num),0))