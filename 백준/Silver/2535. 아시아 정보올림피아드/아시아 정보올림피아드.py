N = int(input())
infos = []
for _ in range(N):
    infos.append(list(map(int,input().split())))

infos.sort(key=lambda x : x[2], reverse=True)


ans = []
country_medals = {}
for country, student, score in infos:
    # country_medals에서 해당 country값의 value(count)가 2이하면
    if country_medals.get(country,0) < 2:
        # ans에 추가하고
        ans.append([country,student])
        # cnt 1개 올리기
        country_medals[country] = country_medals.get(country,0) + 1
    # 3명 다 뽑으면 종료
    if len(ans) == 3:
        break

for i in range(3):
    print(ans[i][0], ans[i][1])