N = int(input())

logs = [input() for _ in range(N)]


cnt = {}
for log in logs:
 name = log.split()[0]
 command = log.split()[1]
 if command == "enter":
  cnt[name] = cnt.get(name,0) + 1
 elif command == "leave":
  cnt[name] = cnt.get(name,0) - 1


ans = []
for company in cnt.items():
 if company[1] == 1:
  ans.append(company[0])
 else:
  continue

ans.sort(reverse=True)
print('\n'.join(map(str,ans)))
