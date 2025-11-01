N = int(input())
idx = []

i = 2
while N != 1:
    if N % i == 0:
        print(i)
        N = N // i
        continue
    else:
        i += 1