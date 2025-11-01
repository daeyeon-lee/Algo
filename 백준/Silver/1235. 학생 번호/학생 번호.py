def findnum(studentnums,k):
    global num
    for i in range(N):
        studentnum = studentnums[i]
        length = len(studentnum)
        num.append(studentnum[length-k:length+1])
    if len(num) != len(set(num)):
        num = []
        k += 1
        findnum(studentnums,k)
    else:
        print(k)
N = int(input())
studentnums = [input() for _ in range(N)]
num = []
k = 1
findnum(studentnums,k)