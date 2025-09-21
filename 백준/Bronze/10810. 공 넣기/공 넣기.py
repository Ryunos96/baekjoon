N, M = map(int, input().split())

arr = [0] * N

for i in range(M):
    a, b, c = map(int, input().split())
    for j in range(b-a+1):
        arr[a+j-1] = c

st = " ".join(map(str, arr))

print(st)