A,B,N = map(int,input().split())

r = A % B


digit = 0
for _ in range(N):
    r *= 10
    digit = r // B
    r %= B

print(digit)

