import sys
input = sys.stdin.readline

def cum_sum():
    for r in range(1, N+1):
        for c in range(1, N+1):
            matrix[r][c]+= matrix[r][c-1]
            matrix[r][c]+= matrix[r-1][c]
            matrix[r][c] -= matrix[r-1][c-1]

def cal_sum(sr, sc, er, ec):
    result = matrix[er][ec]
    result -= matrix[sr-1][ec]
    result -= matrix[er][sc-1]
    result += matrix[sr-1][sc-1]
    return result

N, M = map(int, input().split())
matrix = [[0]*(N+1)]+[[0]+list(map(int, input().split())) for _ in range(N)]
cum_sum()

for _ in range(M):
    sr, sc, er, ec = map(int, input().split())
    print(cal_sum(sr, sc, er, ec))
    