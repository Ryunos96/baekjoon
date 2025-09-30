cover = [[0] * 100 for _ in range(100)]


N = int(input()) # 색종이 수
result = 0
for i in range(N):
    x, y = map(int, input().split()) # 색종이 좌표
    for j in range(x, x + 10):
        for k in range(y, y + 10):
            if cover[j][k] == 1:
                continue
            else:
                cover[j][k] = 1
                result += 1
    
print(result)
