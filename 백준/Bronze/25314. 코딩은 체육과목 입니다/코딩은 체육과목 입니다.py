N = int(input())
ans = ''
num = int(N/4)
for _ in range(num):
    ans += "long" + " "
ans += "int"
print(ans)