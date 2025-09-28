N, M = map(int, input().split())

A = [list(map(int, input().split())) for _ in range(N)]
B = [list(map(int, input().split())) for _ in range(N)]

for i, j in zip(A, B):
    print(*[x + y for x, y in zip(i, j)])