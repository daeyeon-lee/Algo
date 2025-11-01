N = int(input())
arr = [0] + list(map(int,input().split()))

ans = []
for i in range(1,N+1):
    ans.insert(arr[i],i)
print(*ans[::-1])


