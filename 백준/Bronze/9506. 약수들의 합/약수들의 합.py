def perfect_num(num):
    ans = []
    for i in range(1,num):
        if num % i == 0:
            ans.append(i)
        else:
            continue
    if sum(ans) == num:
        print(num, '=', " + ".join(map(str,ans)))
    else:
        print(f"{num} is NOT perfect.")

while True:
    n = int(input())
    if n == -1:
        break
    perfect_num(n)