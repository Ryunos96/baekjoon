M, N = map(int, input().split())

boxes = [list(input()) for _ in range(M)]
result = 64

for i in range(M - 7):
    for j in range(N - 7):
        whitecnt = 0
        blackcnt = 0

        for x in range(i, i + 8):
            for y in range(j, j + 8):
                if (x + y) % 2 == 0:
                    if boxes[x][y] != 'W':
                        whitecnt += 1
                    if boxes[x][y] != 'B':
                        blackcnt += 1
                else:
                    if boxes[x][y] != 'B':
                        whitecnt += 1
                    if boxes[x][y] != 'W':
                        blackcnt += 1
        result = min(result, whitecnt, blackcnt)
print(result)