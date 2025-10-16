N = int(input())

arr = []

for _ in range(N):
    arr.append(list(map(int, input().split())))

if N == 1:
    print(0)
else:
    xmax = max(arr, key=lambda x: x[0])[0]
    ymax = max(arr, key=lambda x: x[1])[1]
    xmin = min(arr, key=lambda x: x[0])[0]
    ymin = min(arr, key=lambda x: x[1])[1]
    print((xmax - xmin) * (ymax - ymin))