while True:
    a,b,c = map(int,input().split())
    ans = 'wrong'
    if a == 0 and b == 0 and c == 0:
        break
    x,y,z = sorted([a,b,c]) # z를 가장 긴변으로 정렬
    if z**2 == (x**2) + (y**2):
        ans = 'right'
    print(ans)