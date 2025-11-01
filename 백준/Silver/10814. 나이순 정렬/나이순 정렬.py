N = int(input())
members = []
for i in range(N):
    age, name = input().split()
    members.append([i,int(age),name])

sorted_members = sorted(members, key=lambda x:(x[1],x[0]))
for j in sorted_members:
    print(j[1],j[2])
