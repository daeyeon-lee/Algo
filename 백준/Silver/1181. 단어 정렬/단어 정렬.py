N = int(input())
arr = [input() for _ in range(N)]

# 중복 제거
arr = set(arr)
arr = list(arr)

# 중복 제거 리스트 중 가장 긴 단어 수 찾기
max_len = max(len(i) for i in arr)

# 가장 긴 단어 수까지만 리스트 만들기
sorted_arr = [[] for _ in range(max_len+1)]

# 길이가 짧은 것부터 정렬
for i in arr:
    sorted_arr[len(i)].append(i)

# 길이가 같으면 사전 순으로 정렬
for i in range(len(sorted_arr)):
    if len(sorted_arr[i]) > 1:
        sorted_arr[i].sort()

# 정답 출력
for j in range(len(sorted_arr)):
    if sorted_arr[j]:
        for k in range(len(sorted_arr[j])):
            print(sorted_arr[j][k])
