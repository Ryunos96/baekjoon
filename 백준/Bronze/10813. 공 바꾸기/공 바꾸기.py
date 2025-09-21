N, M = map(int, input().split())

arr = [0] * N
for i in range(N):
    arr[i] = i+1
temp = 0
for i in range(M):
    a, b = map(int, input().split())
    temp = arr[a-1]
    arr[a-1] = arr[b-1]
    arr[b-1] = temp

st = " ".join(map(str, arr))

print(st)