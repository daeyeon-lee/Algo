T = int(input())
for _ in range(T):
    W = input()
    K = int(input())
    # 3번에서 구한 문자열
    cnt_v = {}
    # 각 문자열 : index값 리스트를 key:value로 저장
    for idx, letter in enumerate(W):
        if letter not in cnt_v:
            cnt_v[letter] = []
        cnt_v[letter].append(idx)

    min_len = 2e21
    max_len = 0

    # K번 이상 등장한 문자열 찾기
    for i, index_list in cnt_v.items():
        if len(index_list) < K:
            continue
        # K개 포함되었을 때 길이 구하기
        for j in range(len(index_list)-K + 1):
            length = index_list[j+K-1] - index_list[j] + 1
            # 최소 길이, 최대 길이 구하기
            if length < min_len:
                min_len = length
            if length > max_len:
                max_len = length

    # K개 이상 나온 문자열이 없는 경우(업데이트 된 적 없는 경우)
    if min_len == 2e21 or max_len == 0:
        print(-1)
    else:
        print(min_len, max_len)