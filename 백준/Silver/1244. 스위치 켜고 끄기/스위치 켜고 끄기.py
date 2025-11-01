swtich_num = int(input())
arr = [0] + list(map(int,input().split()))
student_num = int(input())
for _ in range(student_num):
    gender, num = map(int,input().split())
    
    if gender == 1: # 남학생
        for i in range(1,swtich_num+1):
            if i % num == 0:
                arr[i] = 1 - arr[i]
    if gender == 2: # 여학생
        for i in range(1,swtich_num+1):
            if i == num:
                arr[i] = 1 - arr[i]
                for k in range(1,swtich_num+1):
                    if 1<= i-k <= swtich_num and 1<= i+k <=swtich_num:
                        if arr[i-k] == arr[i+k]:
                            arr[i-k] = 1 - arr[i-k]
                            arr[i+k] = 1 - arr[i+k]
                        else:
                            break
for i in range(1, swtich_num+1, 20):
    print(*arr[i:i+20])
    