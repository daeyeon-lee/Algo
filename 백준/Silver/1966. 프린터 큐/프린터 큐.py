def find_queue(queue, importance):
    if not queue: # 리스트가 비었으면 종료
        return queue

    first_v = queue[0][1]
    if first_v == max(importance): # max값이면 종료
        return queue

    # 현재 리스트에서
    for i in range(1, N):
        if queue[i][1] > first_v:
            queue.append(queue[0])
            queue.pop(0)
            break
    return find_queue(queue, importance)

T = int(input())
for _ in range(T):
    N, M = map(int,input().split())
    values = list(map(int,input().split()))
    queue = []
    printer = []
    for idx, value in enumerate(values):
        queue.append((idx,value))

    while queue:
        importance = []
        for i, v in queue:
            importance.append(v)
        queue = find_queue(queue, importance)

        printer.append(queue[0])
        queue.pop(0)

    for k in range(N):
        if printer[k][0] == M:
            print(k+1)
