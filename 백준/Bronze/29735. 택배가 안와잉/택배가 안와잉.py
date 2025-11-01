# 택배 배송이 끝나는 시점이 퇴근시각과 같거나 그 이후라면 배송하지 않고 퇴근

start_time, finish_time = input().split()
N, T = map(int,input().split()) # N : 브실이 전 배송해야할 택배 수, T : 배달 한건에 걸리는 시간(분)

startHH, startMM = map(int,start_time.split(':'))
finishHH, finishMM = map(int,finish_time.split(':'))

start_mins = startHH * 60 + startMM
finish_mins = finishHH * 60 + finishMM


working_mins = finish_mins-start_mins

oneday_delivers = (working_mins-1) // T


deliver_day = (N+1) // oneday_delivers
deliver_time = ((N+1) % oneday_delivers) * T

if (N+1) % oneday_delivers == 0:
    result_mins = start_mins + (T * oneday_delivers)
    HH = result_mins // 60
    MM = result_mins % 60
    deliver_day -= 1
else:
    result_mins = start_mins + deliver_time
    HH = result_mins // 60
    MM = result_mins % 60


print(deliver_day)
print(f"{HH:02d}:{MM:02d}")