N, M = map(int, input().split())

arr = [0] * N
for i in range(N):
    arr[i] = i+1

for j in range(M):
    A, B = map(int, input().split())
    arr[A-1:B] = arr[A-1:B][::-1]

print(*arr)