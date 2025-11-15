S = input()
cnt = {}
ans = [0] * 26
for i in range(len(S)):
    cnt[S[i]] = cnt.get(S[i],0) + 1

if cnt.get('a'):
    ans[0] = cnt['a']
if cnt.get('b'):
    ans[1] = cnt['b']
if cnt.get('c'):
    ans[2] = cnt['c']
if cnt.get('d'):
    ans[3] = cnt['d']
if cnt.get('e'):
    ans[4] = cnt['e']
if cnt.get('f'):
    ans[5] = cnt['f']
if cnt.get('g'):
    ans[6] = cnt['g']
if cnt.get('h'):
    ans[7] = cnt['h']
if cnt.get('i'):
    ans[8] = cnt['i']
if cnt.get('j'):
    ans[9] = cnt['j']
if cnt.get('k'):
    ans[10] = cnt['k']
if cnt.get('l'):
    ans[11] = cnt['l']
if cnt.get('m'):
    ans[12] = cnt['m']
if cnt.get('n'):
    ans[13] = cnt['n']
if cnt.get('o'):
    ans[14] = cnt['o']
if cnt.get('p'):
    ans[15] = cnt['p']
if cnt.get('q'):
    ans[16] = cnt['q']
if cnt.get('r'):
    ans[17] = cnt['r']
if cnt.get('s'):
    ans[18] = cnt['s']
if cnt.get('t'):
    ans[19] = cnt['t']
if cnt.get('u'):
    ans[20] = cnt['u']
if cnt.get('v'):
    ans[21] = cnt['v']
if cnt.get('w'):
    ans[22] = cnt['w']
if cnt.get('x'):
    ans[23] = cnt['x']
if cnt.get('y'):
    ans[24] = cnt['y']
if cnt.get('z'):
    ans[25] = cnt['z']

print(*ans)

